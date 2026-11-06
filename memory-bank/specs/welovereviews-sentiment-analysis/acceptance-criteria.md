> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Criterios de aceptación

Checklist completa por requisito; estado actualizado según evidencias: revisión humana y cierre completados. La rúbrica externa de 4Geeks no está en el repositorio: cobertura de los criterios enumerados en el adjunto, sin afirmar verificación de una rúbrica adicional.

| Criterio | Comprobación pendiente | Requisito | Tareas | Evidencia prevista |
|---|---|---|---|---|
| AC-WLR-001 | [x] Documentar la pregunta de negocio | REQ-OBJ-001 | TASK-WLR-003, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-002 | [x] Explicar la comparación del sentimiento escrito con 4,5 estrellas | REQ-OBJ-002 | TASK-WLR-003, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-003 | [x] Enumerar las nueve preguntas analíticas solicitadas | REQ-OBJ-003 | TASK-WLR-003, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-004 | [x] Cargar data/raw/reviews.csv | REQ-EDA-001 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-005 | [x] Verificar dimensiones y expectativa de 500 filas | REQ-EDA-002 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-006 | [x] Inspeccionar tipos de las tres columnas | REQ-EDA-003 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-007 | [x] Identificar nulos por columna | REQ-EDA-004 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-008 | [x] Analizar duplicados completos y de texto por separado | REQ-EDA-005 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-009 | [x] Examinar dominio y distribución de rating humano | REQ-EDA-006 | TASK-WLR-001, TASK-WLR-004, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-010 | [x] Analizar longitudes en caracteres, palabras y tokens | REQ-EDA-007 | TASK-WLR-005, TASK-WLR-009, TASK-WLR-022 | TEST-WLR-005: src/explore.ipynb |
| AC-WLR-011 | [x] Extraer insights respaldados por tablas o gráficos | REQ-EDA-008 | TASK-WLR-005, TASK-WLR-022 | TEST-WLR-005: src/explore.ipynb |
| AC-WLR-012 | [x] Documentar conclusiones de la exploración | REQ-EDA-009 | TASK-WLR-005, TASK-WLR-022 | TEST-WLR-005: src/explore.ipynb |
| AC-WLR-013 | [x] Identificar textos vacíos o de espacios | REQ-CLEAN-001 | TASK-WLR-001, TASK-WLR-006, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-014 | [x] Definir tratamiento de nulos sin imputar sentimiento | REQ-CLEAN-002 | TASK-WLR-001, TASK-WLR-006, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-015 | [x] Conservar duplicados con identificadores distintos y justificarlo | REQ-CLEAN-003 | TASK-WLR-001, TASK-WLR-006, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-016 | [x] Preservar las tres columnas originales sin alterar texto | REQ-CLEAN-004 | TASK-WLR-001, TASK-WLR-006, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-017 | [x] Mantener review_id y orden entre entrada y salida | REQ-CLEAN-005 | TASK-WLR-001, TASK-WLR-006, TASK-WLR-019, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-018 | [x] Justificar cada transformación del texto de inferencia | REQ-CLEAN-006 | TASK-WLR-006, TASK-WLR-009, TASK-WLR-022 | TEST-WLR-006: src/explore.ipynb |
| AC-WLR-019 | [x] Verificar predicción para cada una de las 500 reseñas procesables y explicar excepciones | REQ-CLEAN-007 | TASK-WLR-006, TASK-WLR-010, TASK-WLR-019, TASK-WLR-022 | TEST-WLR-006: src/explore.ipynb |
| AC-WLR-020 | [x] Utilizar exclusivamente nlptown/bert-base-multilingual-uncased-sentiment | REQ-MODEL-001 | TASK-WLR-002, TASK-WLR-007, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |
| AC-WLR-021 | [x] Fijar revisión 8f6f4e3a8f70be4b65d3a4a8762b6d781cda240d para modelo y tokenizer | REQ-MODEL-002 | TASK-WLR-002, TASK-WLR-007, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |
| AC-WLR-022 | [x] Cargar modelo y tokenizer una sola vez por ejecución | REQ-MODEL-003 | TASK-WLR-007, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-007: src/explore.ipynb |
| AC-WLR-023 | [x] Reutilizar la instancia en todas las reseñas | REQ-MODEL-004 | TASK-WLR-007, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-007: src/explore.ipynb |
| AC-WLR-024 | [x] Ejecutar inferencia en evaluación sin entrenamiento ni gradientes | REQ-MODEL-005 | TASK-WLR-007, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-007: src/explore.ipynb |
| AC-WLR-025 | [x] Obtener estrellas enteras entre 1 y 5 | REQ-MODEL-006 | TASK-WLR-008, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-026 | [x] Registrar errores de inferencia con review_id sin inventar predicciones | REQ-MODEL-007 | TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-010: src/explore.ipynb |
| AC-WLR-027 | [x] Documentar configuración y versiones efectivas | REQ-MODEL-008 | TASK-WLR-002, TASK-WLR-007, TASK-WLR-009, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |
| AC-WLR-028 | [x] Evaluar lotes frente a ejecución individual y comprobar igualdad de clases | REQ-MODEL-009 | TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-010: src/explore.ipynb |
| AC-WLR-029 | [x] Convertir las cinco etiquetas verificadas a estrellas mediante diccionario explícito | REQ-SENT-001 | TASK-WLR-008, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-030 | [x] Aplicar 1–2 Negative, 3 Neutral y 4–5 Positive | REQ-SENT-002 | TASK-WLR-008, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-031 | [x] Asociar sentimiento a cada reseña procesada | REQ-SENT-003 | TASK-WLR-008, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-032 | [x] Conservar predicted_stars y sentiment como columnas independientes | REQ-SENT-004 | TASK-WLR-008, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-033 | [x] Validar exhaustivamente las cinco clases y rechazar valores inválidos | REQ-SENT-005 | TASK-WLR-008, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-008: src/explore.ipynb |
| AC-WLR-034 | [x] Calcular porcentaje Positive sobre reseñas con predicción válida | REQ-ANALYSIS-001 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-035 | [x] Calcular porcentaje Neutral sobre reseñas con predicción válida | REQ-ANALYSIS-002 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-036 | [x] Calcular porcentaje Negative sobre reseñas con predicción válida | REQ-ANALYSIS-003 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-037 | [x] Calcular conteos y porcentajes de estrellas 1–5 incluyendo ceros | REQ-ANALYSIS-004 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-038 | [x] Calcular media aritmética de predicted_stars válidas | REQ-ANALYSIS-005 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-039 | [x] Comparar media predicha con 4,5 mediante diferencia explícita | REQ-ANALYSIS-006 | TASK-WLR-012, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-012: src/explore.ipynb |
| AC-WLR-040 | [x] Distinguir rating humano, referencia de negocio y sentimiento textual | REQ-ANALYSIS-007 | TASK-WLR-012, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-012: src/explore.ipynb |
| AC-WLR-041 | [x] Documentar discrepancias con identificadores y diferencias | REQ-ANALYSIS-008 | TASK-WLR-012, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-012: src/explore.ipynb |
| AC-WLR-042 | [x] Limitar conclusiones a evidencias observadas sin inferir que 4,5 equivale a 90 % positivo | REQ-ANALYSIS-009 | TASK-WLR-012, TASK-WLR-016, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-012: src/explore.ipynb |
| AC-WLR-043 | [x] Identificar candidatos con predicted_stars en 1–2 y rating en 4–5 | REQ-FN-001 | TASK-WLR-013, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-044 | [x] Identificar discrepancias textuales mediante revisión humana cuando sea necesario | REQ-FN-002 | TASK-WLR-015, TASK-WLR-022 | TEST-WLR-015: src/explore.ipynb |
| AC-WLR-045 | [x] Seleccionar ejemplos reales identificados y declarar si no hay candidatos | REQ-FN-003 | TASK-WLR-013, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-046 | [x] Documentar texto original, rating, predicted_stars y sentiment de los ejemplos | REQ-FN-004 | TASK-WLR-013, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-047 | [x] Analizar patrones compartidos solo si los ejemplos los respaldan | REQ-FN-005 | TASK-WLR-013, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-048 | [x] Formular hipótesis contrastables sobre productos frente a servicios | REQ-FN-006 | TASK-WLR-013, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-049 | [x] Distinguir discrepancia numérica de error confirmado mediante revisión textual | REQ-FN-007 | TASK-WLR-015, TASK-WLR-022 | TEST-WLR-015: src/explore.ipynb |
| AC-WLR-050 | [x] Seleccionar entre 15 y 20 reseñas únicas para revisión real | REQ-VALID-001 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-051 | [x] Incluir distintos sentimientos disponibles y documentar bandas ausentes | REQ-VALID-002 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-052 | [x] Incluir casos discrepantes disponibles y documentar su ausencia | REQ-VALID-003 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-053 | [x] Registrar predicción del modelo en la muestra | REQ-VALID-004 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-054 | [x] Registrar rating humano en la muestra | REQ-VALID-005 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-055 | [x] Registrar interpretación textual de un revisor humano real | REQ-VALID-006 | TASK-WLR-015, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-015: src/explore.ipynb |
| AC-WLR-056 | [x] Documentar errores, ambigüedad y observaciones por review_id | REQ-VALID-007 | TASK-WLR-015, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-015: src/explore.ipynb |
| AC-WLR-057 | [x] Explicar selección estratificada reproducible y sus límites | REQ-VALID-008 | TASK-WLR-014, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-014: src/explore.ipynb |
| AC-WLR-058 | [x] Utilizar src/explore.ipynb como entregable analítico | REQ-NOTEBOOK-001 | TASK-WLR-003, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-059 | [x] Incluir objetivos y preguntas de negocio | REQ-NOTEBOOK-002 | TASK-WLR-003, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-060 | [x] Incluir EDA con evidencias | REQ-NOTEBOOK-003 | TASK-WLR-004, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-004: src/explore.ipynb |
| AC-WLR-061 | [x] Incluir limpieza justificada | REQ-NOTEBOOK-004 | TASK-WLR-006, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-006: src/explore.ipynb |
| AC-WLR-062 | [x] Incluir plan de acción y justificación del modelo obligatorio | REQ-NOTEBOOK-005 | TASK-WLR-006, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-006: src/explore.ipynb |
| AC-WLR-063 | [x] Incluir integración e inferencia real | REQ-NOTEBOOK-006 | TASK-WLR-007, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-007: src/explore.ipynb |
| AC-WLR-064 | [x] Incluir análisis de resultados | REQ-NOTEBOOK-007 | TASK-WLR-011, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-011: src/explore.ipynb |
| AC-WLR-065 | [x] Incluir análisis de posibles falsos negativos | REQ-NOTEBOOK-008 | TASK-WLR-013, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-013: src/explore.ipynb |
| AC-WLR-066 | [x] Incluir validación manual real | REQ-NOTEBOOK-009 | TASK-WLR-015, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-015: src/explore.ipynb |
| AC-WLR-067 | [x] Incluir conclusiones para la account manager | REQ-NOTEBOOK-010 | TASK-WLR-016, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-016: src/explore.ipynb |
| AC-WLR-068 | [x] Insertar markdown breve entre bloques analíticos | REQ-NOTEBOOK-011 | TASK-WLR-016, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-016: src/explore.ipynb |
| AC-WLR-069 | [x] Entregar salidas ejecutadas desde kernel limpio y sin errores | REQ-NOTEBOOK-012 | TASK-WLR-021, TASK-WLR-022 | TEST-WLR-021: src/explore.ipynb |
| AC-WLR-070 | [x] Implementar inferencia independiente en src/app.py | REQ-PROD-001 | TASK-WLR-017, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-071 | [x] Leer dataset original mediante ruta relativa a raíz del proyecto | REQ-PROD-002 | TASK-WLR-001, TASK-WLR-017, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-072 | [x] Cargar modelo una sola vez por ejecución del script | REQ-PROD-003 | TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-018: src/app.py |
| AC-WLR-073 | [x] Inferir las 500 reseñas cuando todas sean procesables | REQ-PROD-004 | TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-018: src/app.py |
| AC-WLR-074 | [x] Incorporar predicted_stars al resultado | REQ-PROD-005 | TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-018: src/app.py |
| AC-WLR-075 | [x] Incorporar sentiment al resultado | REQ-PROD-006 | TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-018: src/app.py |
| AC-WLR-076 | [x] Preservar datos originales y orden de todas las filas | REQ-PROD-007 | TASK-WLR-017, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-077 | [x] Generar data/processed/reviews_with_sentiment.csv | REQ-PROD-008 | TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-019: src/app.py |
| AC-WLR-078 | [x] Permitir python src/app.py sin base de datos ni ejecución del notebook | REQ-PROD-009 | TASK-WLR-017, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-079 | [x] Fijar versiones exactas de dependencias necesarias en requirements.txt | REQ-PROD-010 | TASK-WLR-002, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |
| AC-WLR-080 | [x] Repetir análisis con modelo y dependencias fijados | NFR-001 | TASK-WLR-002, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |
| AC-WLR-081 | [x] Asociar cada predicción a review_id original | NFR-002 | TASK-WLR-001, TASK-WLR-018, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-082 | [x] Preservar contenido original y hash del CSV de entrada | NFR-003 | TASK-WLR-001, TASK-WLR-018, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-001: data/raw/reviews.csv (solo lectura) |
| AC-WLR-083 | [x] Inicializar modelo una vez y evaluar lotes en CPU | NFR-004 | TASK-WLR-007, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-007: src/explore.ipynb |
| AC-WLR-084 | [x] Separar inferencia reutilizable y análisis narrativo | NFR-005 | TASK-WLR-017, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-085 | [x] Comunicar resultados comprensibles a destinataria no técnica | NFR-006 | TASK-WLR-003, TASK-WLR-016, TASK-WLR-021, TASK-WLR-022 | TEST-WLR-003: src/explore.ipynb |
| AC-WLR-086 | [x] Mantener alcance académico sin servicios ni entrenamiento | NFR-007 | TASK-WLR-017, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-087 | [x] Hacer visibles errores sin resultados silenciosamente incorrectos | NFR-008 | TASK-WLR-017, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-017: src/app.py |
| AC-WLR-088 | [x] Ejecutar en Python compatible y comprobar Codespaces cuando esté disponible | NFR-009 | TASK-WLR-002, TASK-WLR-020, TASK-WLR-022 | TEST-WLR-002: requirements.txt |

## Entrega GitHub

- [x] AC-DELIVERY-001: artefactos preparados para GitHub, sin pesos ni secretos; TASK-WLR-022 y TEST-WLR-022. Evidencia: diff revisado y los cuatro entregables esperados. No requiere ni autoriza commit/push.

## Checklist de evaluación solicitada

Los vínculos de cada requisito a tareas y evidencia son los de la tabla anterior. Predicciones, integridad, ejecución, revisión humana y conclusiones verificadas.

- [x] Notebook completo: REQ-NOTEBOOK-001, AC-WLR-058; TASK-WLR-003, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Salidas ejecutadas: REQ-NOTEBOOK-012, AC-WLR-069; TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Objetivos documentados: REQ-OBJ-001, AC-WLR-001; TASK-WLR-003, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] EDA realizado: REQ-EDA-009, AC-WLR-012; TASK-WLR-005, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Insights identificados: REQ-EDA-008, AC-WLR-011; TASK-WLR-005, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Limpieza justificada: REQ-CLEAN-006, AC-WLR-018; TASK-WLR-006, TASK-WLR-009, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Plan de acción explicado: REQ-NOTEBOOK-005, AC-WLR-062; TASK-WLR-006, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Modelo obligatorio integrado: REQ-MODEL-001, AC-WLR-020; TASK-WLR-002, TASK-WLR-007, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Modelo fijado a revisión específica: REQ-MODEL-002, AC-WLR-021; TASK-WLR-002, TASK-WLR-007, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Modelo cargado una sola vez: REQ-MODEL-003, AC-WLR-022; TASK-WLR-007, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] 500 reseñas procesadas: REQ-CLEAN-007, AC-WLR-019; TASK-WLR-006, TASK-WLR-010, TASK-WLR-019, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Estrellas predichas disponibles: REQ-SENT-001, AC-WLR-029; TASK-WLR-008, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Bandas de sentimiento disponibles: REQ-SENT-003, AC-WLR-031; TASK-WLR-008, TASK-WLR-010, TASK-WLR-018, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Distribución positiva calculada: REQ-ANALYSIS-001, AC-WLR-034; TASK-WLR-011, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Distribución neutral calculada: REQ-ANALYSIS-002, AC-WLR-035; TASK-WLR-011, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Distribución negativa calculada: REQ-ANALYSIS-003, AC-WLR-036; TASK-WLR-011, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Comparación con 4,5 estrellas: REQ-ANALYSIS-006, AC-WLR-039; TASK-WLR-012, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Falsos negativos analizados: REQ-FN-007, AC-WLR-049; TASK-WLR-015, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Ejemplos específicos documentados: REQ-FN-003, AC-WLR-045; TASK-WLR-013, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Muestra de 15–20 reseñas revisada: REQ-VALID-001, AC-WLR-050; TASK-WLR-014, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Conclusiones para la account manager: REQ-NOTEBOOK-010, AC-WLR-067; TASK-WLR-016, TASK-WLR-021, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] src/app.py funcional: REQ-PROD-009, AC-WLR-078; TASK-WLR-017, TASK-WLR-019, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] CSV enriquecido generado: REQ-PROD-008, AC-WLR-077; TASK-WLR-019, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Dependencias fijadas: REQ-PROD-010, AC-WLR-079; TASK-WLR-002, TASK-WLR-020, TASK-WLR-022; evidencia de la fila correspondiente.
- [x] Artefactos preparados para entrega en GitHub: AC-DELIVERY-001; TASK-WLR-022; diff y cuatro artefactos revisados.

## Cierre verificado

Todos los criterios cubiertos por artefactos reales. Revisión de 18 textos atribuida a ark el 2026-11-06; notebook reejecutado con las anotaciones sin modificar etiquetas. Cinco discrepancias y tres falsos negativos revisados. Entrega preparada, sin commits/pushes automáticos. Codespaces no ejecutado; portabilidad basada en entorno Python compatible y dependencias fijadas.
