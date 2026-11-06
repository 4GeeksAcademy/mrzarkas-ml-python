> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Investigación técnica

## Fuentes verificadas el 2026-11-06

- [API del modelo](https://huggingface.co/api/models/nlptown/bert-base-multilingual-uncased-sentiment): SHA 8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d, público, no gated; model.safetensors disponible; 167.360.261 parámetros F32.
- [Ficha fijada](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment/blob/8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d/README.md).
- [Configuración fijada](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment/blob/8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d/config.json).
- [Tokenizer fijado](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment/blob/8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d/tokenizer_config.json).

La red sandbox no resolvía huggingface.co; consulta realizada con autorización de acceso externo. Solo metadatos/textos, ningún peso descargado.

## Modelo

BertForSequenceClassification, BERT multilingüe uncased, 12 capas, 12 cabezas y hidden_size 768. Ajustado previamente por sus autores en reseñas de productos; este proyecto no lo entrena. Idiomas de ajuste: inglés, neerlandés, alemán, francés, italiano y español. Clasificación de cinco estrellas: 1 star, 2 stars, 3 stars, 4 stars, 5 stars. Pipeline de text-classification devuelve por entrada label y score de clase predicha, normalmente lista de diccionarios. Validar estructura con versión elegida. score es salida softmax, no precisión calibrada.

Límite verificado: 512 posiciones/tokens, incluidos especiales; tokenización subword, no 512 palabras. Truncamiento a 512 puede ocultar conclusión o contraste final. Medir antes de truncar y documentar IDs afectados; preservar texto original. No introducir segmentación/promedio de ventanas que cambiaría semántica sin nueva decisión.

La ficha publica accuracy exacta en productos ingleses 67 % y off-by-1 95 % sobre 5.000 reseñas de prueba; son resultados del autor en otro dominio, nunca rendimiento de estas 500 reseñas. Ambigüedad, ironía, negaciones y contexto pueden limitar desempeño.

## Integración propuesta

Usar transformers.pipeline('text-classification') en PyTorch, CPU device=-1, modelo y tokenizer con el mismo SHA. Inicializar una vez y reutilizar; inferencia en evaluación sin gradientes. Configurar truncation=True, max_length=512 y lote inicial 8; comparar con lote 1 y usar 1 si memoria o equivalencia de clases falla. No prometer tiempo de ejecución.

AutoTokenizer.from_pretrained facilita inspección de tokens y debe reutilizar el tokenizer de la misma inicialización. AutoModelForSequenceClassification.from_pretrained permite control manual de logits/padding/no_grad, pero añade código innecesario: reservar solo si pipeline no permite configuración requerida. No cargar una segunda instancia para EDA de tokens. Verificar parámetros de API con la versión finalmente resuelta.

Descarga automática con from_pretrained/pipeline y caché Hugging Face fuera del repositorio (HF_HOME puede apuntar a caché externa); primera ejecución necesita red, disco y RAM. Pesos F32 aproximadamente 669 MB decimales, con memoria adicional para activaciones, librerías y tokens: presupuesto real pendiente de medición, sin garantías. Caché de revisión completa posibilita modo offline; caché incompleta debe producir error visible. Preferir safetensors disponible, sin incorporar pesos al Git.

## Reproducibilidad propuesta (estado de la inspección inicial; resolución final más abajo)

Identidad y SHA ya verificados. No usar main/latest para ejecución. Registrar también SHA-256 del CSV, versión Python, plataforma, versiones directas/transitivas, dispositivo, batch_size, max_length, truncamiento y semilla de muestreo 42.

Las versiones exactas de paquetes NO están verificadas: no instaladas en el intérprete y no se ha probado resolución. TASK-WLR-002 debe elegir un Python compatible (preferencia Python 3.13 para alinearse al template, sujeto a wheels), resolver conjunto mínimo pandas, numpy, matplotlib, seaborn, transformers, torch, ipykernel y nbconvert/nbformat; fijar == de directas y transitivas necesarias en requirements.txt y comprobar pip check e importaciones. Documentar decisión sobre dependencias heredadas: retirar solo las ajenas al ejercicio si no tienen consumidores necesarios, o fijarlas si se mantienen. No inventar números de versión ni afirmar lock reproducible hoy. Bloqueo técnico de ejecución hasta resolver entorno; no requiere decisión adicional del usuario más allá de aprobar el plan.

## Dominio: hipótesis que requieren ejemplos reales

Atención/personal, esperas, ambiente y experiencias mixtas de servicios pueden pesar distinto respecto a productos. Lenguaje contextual, ironía y ambigüedad pueden separar rating del texto; una discrepancia no acredita error. Los IDs 250 y 400 muestran mezcla de queja y valoración favorable, pero sus predicciones aún no existen. Revisar patrones en candidatos y muestra real; no extrapolar la muestra dirigida a exactitud poblacional ni imputar causas sin evidencia.

## Resolución verificada tras aprobación

Python 3.13.5 (macOS arm64), Transformers 5.22.2, PyTorch 2.15.0, pandas 3.1.1 y numpy 2.5.4. requirements.txt fija 88 distribuciones directas/transitivas resueltas; pip check Passed, imports y carga del modelo reales Passed. Dependencias ajenas al análisis retiradas del listado; utils.py heredado permanece sin usar ni modificar. Notebook y script comparten funciones de app.py. El modelo se descargó automáticamente a /private/tmp/welovereviews-hf-cache; reejecución offline validada. Codespaces sigue sin prueba empírica. Las afirmaciones de paquetes no instalados anteriores describen la inspección inicial, no el estado actual.
