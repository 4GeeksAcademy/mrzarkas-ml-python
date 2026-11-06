"""Pruebas de contratos y fallos; no descargan ni ejecutan el modelo remoto."""
import csv
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import app


class SentimentTests(unittest.TestCase):
    def setUp(self):
        self.reviews = pd.DataFrame([
            ['1', '5', 'Café, "excelente"\nVolveré.'],
            ['2', '1', 'No me gustó.'],
            ['3', '3', 'Normal.'],
        ], columns=app.ORIGINAL_COLUMNS)

    def classifier(self, texts, **kwargs):
        return [{'label': '5 stars' if 'Volveré' in text else '1 star' if 'No ' in text else '3 stars', 'score': 0.6} for text in texts]

    def test_five_labels_and_reject_invalid(self):
        for label, stars in app.LABEL_STARS.items():
            with self.subTest(label=label):
                classifier = Mock(return_value=[{'label': label}])
                result = app.predict_sentiment(self.reviews.iloc[:1], classifier)
                self.assertEqual(result.iloc[0].predicted_stars, stars)
                self.assertEqual(result.iloc[0].sentiment, app.STAR_SENTIMENT[stars])
        for invalid in [0, 6, None, True, 1.0, '1']:
            with self.assertRaises(ValueError):
                app.map_sentiment(invalid)

    def test_batch_preserves_alignment_and_original(self):
        result = app.predict_sentiment(self.reviews, self.classifier, 2)
        app.validate_results(self.reviews, result)
        self.assertEqual(result.predicted_stars.tolist(), [5, 1, 3])
        pd.testing.assert_frame_equal(self.reviews, result[app.ORIGINAL_COLUMNS])

    def test_blank_text_preserved_without_prediction(self):
        original = self.reviews.copy()
        original.loc[1, 'review_text'] = '  '
        result = app.predict_sentiment(original, self.classifier)
        self.assertEqual(len(result), 3)
        self.assertTrue(pd.isna(result.iloc[1].predicted_stars))
        self.assertEqual(result.iloc[1].processing_status, 'invalid_text')
        app.validate_results(original, result)

    def test_unknown_label_is_not_fabricated(self):
        result = app.predict_sentiment(self.reviews, Mock(return_value=[{'label': 'LABEL_0'}] * 3))
        self.assertTrue(result.predicted_stars.isna().all())
        self.assertTrue((result.processing_status == 'inference_error').all())
        app.validate_results(self.reviews, result)

    def test_batch_error_isolated_to_one_row(self):
        def classifier(texts, **kwargs):
            if any('No ' in text for text in texts):
                raise RuntimeError('fallo simulado')
            return self.classifier(texts, **kwargs)
        result = app.predict_sentiment(self.reviews, classifier)
        self.assertEqual(result.processing_status.tolist(), ['ok', 'inference_error', 'ok'])
        self.assertTrue(pd.isna(result.iloc[1].predicted_stars))

    def test_bad_output_cardinality_is_visible(self):
        result = app.predict_sentiment(self.reviews, Mock(return_value=[]))
        self.assertTrue((result.processing_status == 'inference_error').all())

    def test_strict_csv_and_contract_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'reviews.csv'
            self.reviews.to_csv(path, index=False)
            loaded = app.load_reviews(path, 3)
            pd.testing.assert_frame_equal(loaded, self.reviews)
            with self.assertRaises(ValueError):
                app.load_reviews(path, 500)
            for content in ['wrong,rating,review_text\n1,5,text\n', 'review_id,rating,review_text\n1,5,text,extra\n', 'review_id,rating,review_text\n1,5,"unterminated']:
                path.write_text(content)
                with self.assertRaises((ValueError, csv.Error)):
                    app.load_reviews(path, 1)
        with self.assertRaises(FileNotFoundError):
            app.load_reviews(Path('/private/tmp/nonexistent-wlr.csv'))
        for column, value in [('review_id', '1'), ('rating', '6')]:
            invalid = self.reviews.copy()
            invalid.loc[1, column] = value
            with self.assertRaises(ValueError):
                app.validate_reviews(invalid, 3)

    def test_roundtrip_characters_and_failures(self):
        original = self.reviews.copy()
        original.loc[1, 'review_text'] = ''
        result = app.predict_sentiment(original, self.classifier)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'result.csv'
            app.save_results(original, result, path)
            restored = pd.read_csv(path, keep_default_na=False, dtype=str)
            pd.testing.assert_frame_equal(original, restored[app.ORIGINAL_COLUMNS])
            self.assertEqual(restored.iloc[1].predicted_stars, '')
            previous = path.read_bytes()
            with patch('app.os.replace', side_effect=PermissionError('simulado')):
                with self.assertRaises(PermissionError):
                    app.save_results(original, result, path)
            self.assertEqual(previous, path.read_bytes())
            self.assertEqual(list(Path(directory).iterdir()), [path])
        with self.assertRaises(ValueError):
            app.save_results(original, result, app.INPUT_PATH)

    def test_main_loads_once_and_reports_global_error(self):
        model = Mock(side_effect=self.classifier)
        model.tokenizer.side_effect = lambda text, **kwargs: {'input_ids': [1, 2, 3]}
        with patch('app.load_reviews', return_value=self.reviews), patch('app.load_sentiment_model', return_value=model) as load, patch('app.save_results'):
            self.assertEqual(app.main([]), 0)
            load.assert_called_once_with()
        with patch('app.load_reviews', return_value=self.reviews), patch('app.load_sentiment_model', side_effect=RuntimeError('caché incompleta')), patch('app.save_results') as save:
            self.assertEqual(app.main([]), 1)
            save.assert_not_called()

    def test_token_count_includes_specials_and_traces_long(self):
        model = Mock()
        model.tokenizer.side_effect = [{'input_ids': list(range(512))}, {'input_ids': list(range(513))}, {'input_ids': [1, 2]}]
        with self.assertLogs(app.LOGGER, level='WARNING') as captured:
            self.assertEqual(app.token_lengths(self.reviews, model), [512, 513, 2])
        self.assertIn('review_id=2', captured.output[0])
        for call in model.tokenizer.call_args_list:
            self.assertFalse(call.kwargs['truncation'])


if __name__ == '__main__':
    unittest.main()
