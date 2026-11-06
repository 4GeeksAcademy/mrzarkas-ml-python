"""Inferencia reproducible de WeLoveReviews, sin entrenamiento ni base de datos."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import os
from pathlib import Path
import sys
import tempfile

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
MODEL_REVISION = "8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d"
MAX_LENGTH = 512
DEFAULT_BATCH_SIZE = 8
ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT / "data/raw/reviews.csv"
OUTPUT_PATH = ROOT / "data/processed/reviews_with_sentiment.csv"
ORIGINAL_COLUMNS = ["review_id", "rating", "review_text"]
DERIVED_COLUMNS = ["predicted_stars", "sentiment", "processing_status", "processing_error"]
LABEL_STARS = {"1 star": 1, "2 stars": 2, "3 stars": 3, "4 stars": 4, "5 stars": 5}
STAR_SENTIMENT = {1: "Negative", 2: "Negative", 3: "Neutral", 4: "Positive", 5: "Positive"}
LOGGER = logging.getLogger(__name__)


def load_reviews(path: Path = INPUT_PATH, expected_count: int = 500):
    """Leer estrictamente sin modificar contenido ni interpretar NA como nulo."""
    import pandas as pd

    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, strict=True)
        try:
            columns = next(reader)
        except StopIteration as exc:
            raise ValueError("CSV vacío") from exc
        if columns != ORIGINAL_COLUMNS:
            raise ValueError(f"Columnas esperadas: {ORIGINAL_COLUMNS}; recibidas: {columns}")
        rows = list(reader)
        if any(len(row) != len(columns) for row in rows):
            raise ValueError("CSV inválido: número de campos inconsistente")
    reviews = pd.DataFrame(rows, columns=columns)
    validate_reviews(reviews, expected_count)
    return reviews


def validate_reviews(reviews, expected_count: int = 500):
    if list(reviews.columns) != ORIGINAL_COLUMNS:
        raise ValueError(f"Columnas obligatorias: {ORIGINAL_COLUMNS}")
    if len(reviews) != expected_count:
        raise ValueError(f"Se esperaban {expected_count} reseñas; recibidas {len(reviews)}")
    ids = reviews["review_id"].astype(str)
    if not ids.str.fullmatch(r"[0-9]+").all():
        raise ValueError("review_id debe ser entero no vacío")
    if ids.map(int).duplicated().any():
        raise ValueError("review_id duplicado")
    if not reviews["rating"].astype(str).str.fullmatch(r"[1-5]").all():
        raise ValueError("rating debe pertenecer a 1–5")


def map_sentiment(stars: int) -> str:
    if type(stars) is not int or stars not in STAR_SENTIMENT:
        raise ValueError(f"Estrellas inválidas: {stars!r}")
    return STAR_SENTIMENT[stars]


def load_sentiment_model():
    """Una única inicialización; caché Hugging Face fuera del repositorio."""
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

    # Limitar oversubscription en CPU, sin cambiar el modelo ni su precisión.
    torch.set_num_threads(min(4, os.cpu_count() or 1))
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, revision=MODEL_REVISION)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, revision=MODEL_REVISION, use_safetensors=True
    )
    if model.config.id2label != {i: label for i, label in enumerate(LABEL_STARS)}:
        raise ValueError("Etiquetas remotas inesperadas")
    model.eval()
    model.requires_grad_(False)
    return pipeline("text-classification", model=model, tokenizer=tokenizer, device=-1)


def token_lengths(reviews, classifier):
    """Medir incluyendo especiales antes de truncar, reutilizando tokenizer."""
    lengths = []
    for row in reviews.itertuples(index=False):
        text = row.review_text
        count = len(classifier.tokenizer(text, truncation=False)["input_ids"]) if isinstance(text, str) and text.strip() else 0
        lengths.append(count)
        if count > MAX_LENGTH:
            LOGGER.warning("review_id=%s: %s tokens; truncamiento a %s", row.review_id, count, MAX_LENGTH)
    return lengths


def predict_sentiment(reviews, classifier, batch_size: int = DEFAULT_BATCH_SIZE):
    """Mantener orden y filas; lotes fallidos se aíslan sin cargar otro modelo."""
    import pandas as pd

    if type(batch_size) is not int or batch_size < 1:
        raise ValueError("batch_size debe ser entero positivo")
    result = reviews.copy(deep=True).reset_index(drop=True)
    result["predicted_stars"] = pd.Series(pd.NA, index=result.index, dtype="Int64")
    result["sentiment"] = ""
    result["processing_status"] = "invalid_text"
    result["processing_error"] = "Texto vacío o no textual"
    indices = [i for i, text in enumerate(result["review_text"]) if isinstance(text, str) and text.strip()]

    def assign(index, prediction):
        if not isinstance(prediction, dict) or prediction.get("label") not in LABEL_STARS:
            raise ValueError(f"Etiqueta o salida inesperada: {prediction!r}")
        stars = LABEL_STARS[prediction["label"]]
        result.at[index, "predicted_stars"] = stars
        result.at[index, "sentiment"] = map_sentiment(stars)
        result.at[index, "processing_status"] = "ok"
        result.at[index, "processing_error"] = ""

    def fail(index, error):
        result.at[index, "predicted_stars"] = pd.NA
        result.at[index, "sentiment"] = ""
        result.at[index, "processing_status"] = "inference_error"
        result.at[index, "processing_error"] = f"{type(error).__name__}: {error}"
        LOGGER.error("review_id=%s: %s", result.at[index, "review_id"], error)

    for offset in range(0, len(indices), batch_size):
        batch = indices[offset:offset + batch_size]
        texts = result.loc[batch, "review_text"].tolist()
        try:
            predictions = classifier(texts, batch_size=batch_size, truncation=True, max_length=MAX_LENGTH)
            if not isinstance(predictions, list) or len(predictions) != len(batch):
                raise ValueError("Número de predicciones distinto del lote")
        except Exception as batch_error:
            LOGGER.warning("Fallo de lote; aislando filas: %s", batch_error)
            for index in batch:
                try:
                    predictions = classifier([result.at[index, "review_text"]], batch_size=1, truncation=True, max_length=MAX_LENGTH)
                    if not isinstance(predictions, list) or len(predictions) != 1:
                        raise ValueError("Salida individual inválida")
                    assign(index, predictions[0])
                except Exception as error:
                    fail(index, error)
        else:
            for index, prediction in zip(batch, predictions):
                try:
                    assign(index, prediction)
                except Exception as error:
                    fail(index, error)
    return result


def validate_results(original, result):
    import pandas as pd

    if list(result.columns) != ORIGINAL_COLUMNS + DERIVED_COLUMNS:
        raise ValueError("Esquema de salida inesperado")
    pd.testing.assert_frame_equal(
        original.reset_index(drop=True), result[ORIGINAL_COLUMNS].reset_index(drop=True), check_dtype=False
    )
    for row in result.itertuples(index=False):
        if row.processing_status == "ok":
            if pd.isna(row.predicted_stars) or row.predicted_stars not in STAR_SENTIMENT:
                raise ValueError("Predicción ausente/inválida en fila ok")
            if row.sentiment != STAR_SENTIMENT[row.predicted_stars] or row.processing_error:
                raise ValueError("Banda o error inconsistente en fila ok")
        elif row.processing_status in {"invalid_text", "inference_error"}:
            if not pd.isna(row.predicted_stars) or row.sentiment or not row.processing_error:
                raise ValueError("Predicción ficticia o error ausente en fila fallida")
        else:
            raise ValueError("Estado de procesamiento desconocido")


def save_results(original, result, path: Path = OUTPUT_PATH):
    """Validar antes y después de escribir; renombrado atómico al final."""
    import pandas as pd

    path = Path(path)
    if path.resolve() == INPUT_PATH.resolve():
        raise ValueError("La salida no puede sobrescribir el dataset original")
    validate_results(original, result)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="", dir=path.parent, suffix=".csv", delete=False) as stream:
            temporary = Path(stream.name)
            result.to_csv(stream, index=False)
        restored = pd.read_csv(temporary, keep_default_na=False, dtype=str)
        restored["predicted_stars"] = pd.to_numeric(restored["predicted_stars"], errors="coerce").astype("Int64")
        validate_results(original, restored)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if args.batch_size < 1:
            raise ValueError("batch_size debe ser positivo")
        input_hash = hashlib.sha256(INPUT_PATH.read_bytes()).hexdigest()
        reviews = load_reviews()
        classifier = load_sentiment_model()
        lengths = token_lengths(reviews, classifier)
        result = predict_sentiment(reviews, classifier, args.batch_size)
        if hashlib.sha256(INPUT_PATH.read_bytes()).hexdigest() != input_hash:
            raise ValueError("El dataset original cambió durante la ejecución")
        save_results(reviews, result)
        failed = int((result["processing_status"] != "ok").sum())
        print(json.dumps({"model": MODEL_NAME, "revision": MODEL_REVISION, "input_sha256": input_hash,
                          "device": "cpu", "batch_size": args.batch_size, "max_length": MAX_LENGTH,
                          "rows": len(result), "failed": failed, "truncated": sum(x > MAX_LENGTH for x in lengths),
                          "output": str(OUTPUT_PATH)}, ensure_ascii=False, indent=2))
        return 1 if failed else 0
    except Exception as error:
        LOGGER.error("Ejecución fallida: %s. No se publica un nuevo resultado; cualquier salida previa permanece.", error)
        return 1


if __name__ == "__main__":
    sys.exit(main())
