> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Diseño propuesto

## Responsabilidades y flujo

Notebook: reviews.csv → carga/validación → EDA/insights → limpieza justificada → plan/modelo → inferencia → resultados/comparación → falsos negativos → revisión humana → conclusiones. Orden de secciones obligatorio: 1 objetivos; 2 carga y descripción; 3 EDA; 4 insights; 5 limpieza; 6 plan; 7 justificación; 8 integración; 9 inferencia; 10 resultados; 11 comparación con 4,5; 12 falsos negativos; 13 validación manual; 14 conclusiones. Markdown breve, gráficos legibles y salidas ejecutadas. Es el único informe analítico de entrega.

Script: reviews.csv → load_reviews/validate_reviews → load_sentiment_model una vez → predict_sentiment → map_sentiment → save_results → reviews_with_sentiment.csv. main bajo guardia __name__; rutas basadas en __file__, no cwd. No gráficos, EDA ni anotaciones manuales. Sustituir arranque db_connect existente; no necesita tocar utils.py ni configurar BD. Notebook podrá importar funciones puras de app.py una vez extraídas; no ejecutar main al importar.

## DES-OBJ / DES-NOTEBOOK

Preguntas y narrativa definidas en context.md; 14 secciones anteriores. Explicar cobertura, referencia externa y datos reales, sin informe Markdown sustituto.

## DES-EDA / DES-CLEAN / DES-PROD: contrato

Entrada existente: review_id entero único, rating entero 1–5, review_text cadena UTF-8. Mantener valores originales de estas tres columnas y orden. Leer sin normalización destructiva de texto ni coerción silenciosa. Esperado 500 filas; desviación detiene ejecución normal y requiere aclarar fuente antes de nueva ejecución. La comparación original/salida es semántica campo a campo (CSV puede cambiar quoting); archivo original mantiene su hash.

Salida propuesta: review_id, rating, review_text, predicted_stars (entero nullable 1–5), sentiment (Negative/Neutral/Positive nullable), processing_status (ok/invalid_text/inference_error), processing_error (texto vacío en éxito). Estas columnas nuevas no existen aún. Estados/error necesarios para no ocultar fallos; no se añaden score/diferencia al CSV, se pueden calcular en notebook. CSV UTF-8, sin índice. No eliminar duplicados de texto con diferentes IDs. La única limpieza prevista es detectar espacios/vacíos para elegibilidad: no limpiar signos, negaciones, acentos o mayúsculas manualmente; uncased lo gestiona tokenizer. Un texto procesable recibe ambas predicciones; uno inválido conserva fila con campos derivados vacíos y explicación.

## DES-MODEL / DES-SENT

Modelo/revisión y configuración en research.md. Diccionario label→1–5 exacto; bandas 1/2 Negative,3 Neutral,4/5 Positive. Etiqueta inesperada no se interpreta mediante heurística. Clasificador recibe solo review_text, nunca rating, para evitar fuga. Carga única por proceso/notebook Run All. Tokenizar sin truncar para diagnóstico; inferir con 512 incluidos especiales; registrar IDs truncados en notebook/log. Batch 8 condicionado a equivalencia de clases frente a 1 y memoria.

## DES-ANALYSIS / DES-FN / DES-VALID

Denominador: N_ok; publicar también N_total y fallidos. Si N_ok=0, no calcular porcentajes/media; error visible. Conteos por banda y estrellas incluyen categorías de cero. Media predicha = suma estrellas/N_ok; diferencia = media predicha−4,5. Media humana muestral independiente; no asumir que es la referencia externa ni que estrellas se convierten linealmente en porcentaje positivo.

Candidatos a falsos negativos: rating>=4 y predicted_stars<=2. Tabla con review_id, texto, ambas estrellas y banda; sin candidatos, informar ausencia. Error textual solo confirmado mediante revisión humana real independiente de rating, con posibilidad Ambiguous. No estimar accuracy de sentimiento usando rating como verdad textual.

Muestra propuesta: 18 IDs, semilla 42, sin reemplazo; hasta 6 por banda disponible, incluyendo al menos un candidato discrepante por banda si existe; redistribuir cupos de bandas escasas entre disponibles hasta 18. Orden estable por review_id antes de muestreo. Mantener modelo/rating, manual_sentiment (Negative/Neutral/Positive/Ambiguous), razones, revisor y fecha en tabla del notebook. Revisar texto preferiblemente antes de consultar predicción/rating para reducir anclaje. Anotaciones reales necesarias; no rellenar con IA. Muestra dirigida no representa precisión poblacional.

## DES-NFR: robustez y sencillez

Dataset ausente, CSV inválido, columna faltante, ID duplicado, rating inválido o conteo distinto: mensaje concreto y exit code no cero antes de inferencia. Fallo global de carga/red/caché: detener sin producir nuevo resultado. Fallo individual: estado e ID, sin inventar estrellas; publicación parcial solo con estados explícitos y salida no cero. Para esta entrada válida, aceptación exige 500 ok; las excepciones no satisfacen ese criterio silenciosamente. Fallo de escritura: temporal en processed y renombrado solo tras validar, no truncar resultado anterior. Informar si artefacto previo permanece para evitar confundirlo con ejecución actual. Mensajes no necesitan volcar reseñas completas fuera del notebook.

No añadir servicios, entrenamiento, gestión de modelos en models/ ni infraestructura excesiva. Tests estándar mínimos y notebook narrativo. Dependencias se fijan en preparación antes de inferir; comprobar CPU y Codespaces sin alterar template por defecto. Artefactos ejecutados fuera de memory-bank.
