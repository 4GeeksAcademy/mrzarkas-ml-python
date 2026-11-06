> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Estrategia de comprobación

Propuesta mínima: unittest de la biblioteca estándar para mapeo, integridad, carga única y errores con mocks; ejecución real separada para integración. No descargar modelo en tests unitarios. Las secciones siguientes describen la estrategia inicial; los resultados de ejecución y cierre se registran al final.

## TEST-WLR-001 — Confirmar entrada y trazabilidad

**Tarea:** TASK-WLR-001. **Método:** Lectura con csv/pandas; IDs 1–500 únicos, tres columnas, 500 filas; comparar hash original, nulos y duplicados completos/textuales.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** data/raw/reviews.csv (solo lectura), src/explore.ipynb. Estado Pending.

## TEST-WLR-002 — Fijar entorno reproducible

**Tarea:** TASK-WLR-002. **Método:** python --version, python -m pip check y lista de versiones exactas; SHA verificado para modelo y tokenizer. No declarar compatibilidad antes de instalación real.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** requirements.txt, src/explore.ipynb. Estado Pending.

## TEST-WLR-003 — Redactar objetivos del notebook

**Tarea:** TASK-WLR-003. **Método:** Revisión manual: pregunta principal, nueve preguntas y destinataria presentes; 4,5 no tratado como porcentaje.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-004 — Explorar calidad y valoraciones

**Tarea:** TASK-WLR-004. **Método:** Comprobar tablas de dimensiones, tipos, nulos y ratings 1–5; separar duplicación de contenido e ID.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-005 — Explorar longitudes e insights

**Tarea:** TASK-WLR-005. **Método:** Contrastar medidas de longitud e insights con datos; no extrapolar idiomas sin evidencia.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-006 — Definir limpieza y plan de acción

**Tarea:** TASK-WLR-006. **Método:** Comprobar textos vacíos/nulos, duplicados conservados y transformaciones justificadas; igualdad de originales.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-007 — Integrar carga única del modelo

**Tarea:** TASK-WLR-007. **Método:** Mock contador de carga: una inicialización; modelo/SHA exactos, CPU, evaluación y sin entrenamiento.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-008 — Validar etiquetas y sentimiento

**Tarea:** TASK-WLR-008. **Método:** Test parametrizado de etiquetas 1 star/2 stars/3 stars/4 stars/5 stars y mapeo 1,2 Negative;3 Neutral;4,5 Positive. Rechazar 0,6,None y etiqueta desconocida.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-009 — Medir tokens y truncamiento

**Tarea:** TASK-WLR-009. **Método:** Casos límite 512 y >512 tokens incluyendo especiales; truncamiento trazado y texto original intacto.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-010 — Ejecutar inferencia y evaluar lotes

**Tarea:** TASK-WLR-010. **Método:** 500 salidas alineadas por ID si todas válidas; lote 8 vs 1 con misma clase; fallos simulados sin etiquetas inventadas.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-011 — Calcular distribuciones y media

**Tarea:** TASK-WLR-011. **Método:** Recalcular conteos y media desde predicciones; porcentajes sin redondear suman 100 % (tolerancia 1e-8), redondeados a 2 decimales dentro de 0,02 puntos.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-012 — Comparar referencia y discrepancias

**Tarea:** TASK-WLR-012. **Método:** Verificar media predicha menos 4,5 y diferencia frente a media rating; candidatos correctos; no afirmar causalidad ni 90 %.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-013 — Analizar candidatos a falsos negativos

**Tarea:** TASK-WLR-013. **Método:** Revisión manual de IDs y textos reales; comprobar filtro, ausencia de candidatos y separación discrepancia/error.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-014 — Seleccionar muestra manual

**Tarea:** TASK-WLR-014. **Método:** 18 IDs únicos, semilla 42, cuotas y bandas disponibles; casos discrepantes incluidos cuando existan.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-015 — Realizar revisión humana

**Tarea:** TASK-WLR-015. **Método:** Revisión humana: autor y fecha, lectura efectiva, interpretación textual y razones; no sustituir con otra IA ni fabricar anotaciones.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-016 — Redactar conclusiones de negocio

**Tarea:** TASK-WLR-016. **Método:** Revisión manual: conclusiones enlazan cifras y ejemplos, responden negocio y declaran límites.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-017 — Extraer carga y validación al script

**Tarea:** TASK-WLR-017. **Método:** python src/app.py funciona desde raíz y por ruta absoluta desde otro directorio; no depende de DATABASE_URL; simular fichero ausente, CSV malformado y columna faltante.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/app.py. Estado Pending.

## TEST-WLR-018 — Extraer inferencia reproducible

**Tarea:** TASK-WLR-018. **Método:** Tests con mocks: misma instancia y mapeo, alineación de lotes; errores de carga/caché y etiquetas desconocidas visibles.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/app.py, src/explore.ipynb. Estado Pending.

## TEST-WLR-019 — Exportar y verificar CSV

**Tarea:** TASK-WLR-019. **Método:** Releer salida CSV UTF-8 sin índice; 500 IDs, originales idénticos, estrellas/bandas válidas; simular permisos de escritura y error de fila sin salida engañosa.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** src/app.py, data/processed/reviews_with_sentiment.csv. Estado Pending.

## TEST-WLR-020 — Verificar ruta de producción

**Tarea:** TASK-WLR-020. **Método:** python -m unittest discover -s tests; python src/app.py; python -m pip check. Prueba real de modelo distinta de unitarias con mocks. Verificar pesos ausentes de git y configuración.

**Tipo:** Automatizable; integración real cuando interviene modelo o entorno. **Evidencia:** tests/test_app.py (propuesto), src/app.py, data/processed/reviews_with_sentiment.csv. Estado Pending.

## TEST-WLR-021 — Ejecutar notebook completo

**Tarea:** TASK-WLR-021. **Método:** Kernel limpio y Run All, o python -m jupyter nbconvert --to notebook --execute --inplace src/explore.ipynb; ninguna salida error. Igualdad de clases notebook/CSV por ID y configuración. Revisar gráficos y markdown.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb. Estado Pending.

## TEST-WLR-022 — Auditar entrega y aceptación

**Tarea:** TASK-WLR-022. **Método:** Auditar checklist de acceptance-criteria.md, hash original, cuatro entregables, diff sin pesos/secretos y requisitos cubiertos. No commit/push.

**Tipo:** Manual/analítico; cálculos verificables automatizables. **Evidencia:** src/explore.ipynb, src/app.py, requirements.txt, data/processed/reviews_with_sentiment.csv. Estado Pending.

## Casos transversales

Conteo diferente de 500, ID duplicado, rating fuera de dominio y CSV roto: detener con error antes de inferir. Texto vacío: preservar fila con estado invalid_text y campos predichos vacíos, informar cobertura. Fallo individual: estado inference_error e ID; errores globales de modelo impiden publicación. CSV parcial solo con estados explícitos y exit code no cero. Tests de caracteres incluyen acentos, comas, comillas y saltos de línea. La validación humana de muestra dirigida no estima precisión poblacional ni convierte rating en verdad del texto.

## Resultados de ejecución (2026-11-06)

TEST-WLR-001 a 014 y 017 a 020: Passed según notebook, CSV y tests de producción. TEST-WLR-015: Pending, revisión humana real. TEST-WLR-016: In Progress, conclusiones descriptivas provisionales. TEST-WLR-021: ejecución técnica Passed (15 celdas de código, sin errores, tres gráficos legibles, predicciones idénticas al CSV); cierre integral pendiente de revisión humana. TEST-WLR-022: In Progress, auditoría técnica correcta y revisión humana pendiente. unittest: 10 tests Passed; pip check Passed; script ejecutado offline desde otro directorio con 500 ok.

## Verificación tras revisión humana

TEST-WLR-015/016/021/022 Passed: 18 filas con etiquetas válidas y autor/fecha/razón; notebook ejecutado desde kernel limpio sin errores y conclusiones sustentadas por anotaciones. Se conservan las etiquetas humanas de casos mixtos. Las comprobaciones de implementación previas siguen vigentes; no se cambió app.py ni sus tests en este cierre.
