> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Plan de implementación

Secuencia propuesta, sin estimaciones de duración. Prerrequisito global: aprobación expresa del usuario. research.md registra la resolución verificada de versiones; no bloquear documentación ni simular su verificación.

## PLAN-01 — Preparación

**Objetivo:** completar preparación con evidencia real.
**Entradas:** repositorio y CSV verificados; aprobación GATE-05.
**Tareas:** TASK-WLR-001, TASK-WLR-002.
**Dependencias:** las aristas de tasks.md prevalecen; GATE-05.
**Riesgos:** compatibilidad, conectividad y origen del dataset.
**Entregables:** data/raw/reviews.csv (solo lectura), requirements.txt, src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entorno sin resolver o revisión no accesible.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-02 — Notebook: objetivos y EDA

**Objetivo:** completar notebook: objetivos y eda con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-003, TASK-WLR-004, TASK-WLR-005, TASK-WLR-006.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-03 — Integración del modelo

**Objetivo:** completar integración del modelo con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-007, TASK-WLR-008, TASK-WLR-009, TASK-WLR-010.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-04 — Análisis de resultados

**Objetivo:** completar análisis de resultados con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-011, TASK-WLR-012, TASK-WLR-013.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-05 — Validación y conclusiones

**Objetivo:** completar validación y conclusiones con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-014, TASK-WLR-015, TASK-WLR-016.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-06 — Producción

**Objetivo:** completar producción con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-017, TASK-WLR-018, TASK-WLR-019.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** data/processed/reviews_with_sentiment.csv, src/app.py, src/explore.ipynb.
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## PLAN-07 — Verificación y entrega

**Objetivo:** completar verificación y entrega con evidencia real.
**Entradas:** artefactos y verificaciones de las tareas predecesoras en tasks.md.
**Tareas:** TASK-WLR-020, TASK-WLR-021, TASK-WLR-022.
**Dependencias:** las aristas de tasks.md prevalecen; fases anteriores para cada tarea dependiente; PLAN-06 puede comenzar tras inferencia validada, pero entrega requiere PLAN-05.
**Riesgos:** errores de datos/modelo, truncamiento, interpretación y reproducibilidad; ver risks-and-decisions.md.
**Entregables:** data/processed/reviews_with_sentiment.csv, requirements.txt, src/app.py, src/explore.ipynb, tests/test_app.py (propuesto).
**Aceptación:** todos los criterios de sus tareas y TEST-WLR correspondientes aprobados; sin alterar originales.
**Bloqueo:** entradas no validadas o fallos de checks; revisión humana real pendiente en PLAN-05.
**Evidencia de finalización:** resultados reales en entregables enumerados y checklist vinculada; no estados Completed sin evidencia.

## Quality Gates

| Gate | Estado | Evidencia / condición |
|---|---|---|
| GATE-01 Contexto validado | Passed | Lectura repo, datos y restricciones registrada en context.md. |
| GATE-02 Especificación completa | Passed | 79 funcionales y 9 NFR, EARS, criterios y auditoría documental. |
| GATE-03 Diseño aprobado | Passed | Aprobación expresa del usuario: «aprobado». |
| GATE-04 Plan preparado | Passed | 7 fases, 22 tareas, riesgos y trazabilidad completa. |
| GATE-05 Autorización implementación | Passed | Aprobación expresa del usuario: «aprobado». |

Orden topológico recomendado: TASK-WLR-001 a TASK-WLR-022. Primer paso tras aprobación: TASK-WLR-001; después TASK-WLR-002 resuelve versiones exactas antes de integrar modelo. Estado final: 22 tareas completadas; revisión humana TASK-WLR-015 verificada y conclusiones finales ejecutadas.

## Seguimiento de implementación

Se ejecutaron 500 predicciones reales en CPU, sin fallos ni truncamientos. Notebook con 15 celdas de código ejecutadas, equivalencia de lotes y CSV verificada; 10 tests y pip check Passed. Cierre de TASK-WLR-016/021/022 verificado tras revisión humana de TASK-WLR-015. No se ha probado Codespaces. La revisión humana efectiva se asigna a TASK-WLR-015, evitando exigirla en TASK-WLR-013 antes de seleccionar la muestra.

## Cierre final

TASK-WLR-015/016/021/022 Completed. Revisión confirmada por el usuario, 18 anotaciones de ark del 2026-11-06. Notebook reejecutado, sin errores, con 13 acuerdos, 5 discrepancias y falsos negativos textuales revisados IDs 15/254/489. Datos y predicciones de producción intactos. Todos los gates Passed; sin commit/push.
