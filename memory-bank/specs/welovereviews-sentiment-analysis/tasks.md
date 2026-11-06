> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Tareas ejecutables

Estados permitidos: Pending, In Progress, Blocked, Completed. Seguimiento final: 22 Completed, con revisión humana real de 18 textos por ark el 2026-11-06. Cambiar a Completed solo con evidencia real. GATE-05 es prerrequisito global; la revisión humana real es condición de TASK-WLR-015.

## TASK-WLR-001 — Confirmar entrada y trazabilidad

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-01

### Objetivo
Revalidar esquema, 500 IDs únicos, calidad y SHA-256; acordar conservación de duplicados.

### Requisitos relacionados
- REQ-EDA-001
- REQ-EDA-002
- REQ-EDA-003
- REQ-EDA-004
- REQ-EDA-005
- REQ-EDA-006
- REQ-CLEAN-001
- REQ-CLEAN-002
- REQ-CLEAN-003
- REQ-CLEAN-004
- REQ-CLEAN-005
- REQ-PROD-002
- NFR-002
- NFR-003

### Archivos afectados
- `data/raw/reviews.csv (solo lectura)`
- `src/explore.ipynb`

### Dependencias
- GATE-05; sin tarea predecesora.

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Revalidar esquema, 500 IDs únicos, calidad y SHA-256; acordar conservación de duplicados.
3. Ejecutar TEST-WLR-001 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Revalidar esquema, 500 IDs únicos, calidad y SHA-256; acordar conservación de duplicados.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-001 aprobada.

### Verificación
TEST-WLR-001 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `data/raw/reviews.csv (solo lectura)`, `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-002 — Fijar entorno reproducible

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-01

### Objetivo
Crear entorno aislado compatible; resolver versiones exactas, registrar Python y pip check; verificar SHA remoto.

### Requisitos relacionados
- REQ-MODEL-001
- REQ-MODEL-002
- REQ-MODEL-008
- REQ-PROD-010
- NFR-001
- NFR-009

### Archivos afectados
- `requirements.txt`
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-001

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Crear entorno aislado compatible; resolver versiones exactas, registrar Python y pip check; verificar SHA remoto.
3. Ejecutar TEST-WLR-002 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Crear entorno aislado compatible; resolver versiones exactas, registrar Python y pip check; verificar SHA remoto.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-002 aprobada.

### Verificación
TEST-WLR-002 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `requirements.txt`, `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-003 — Redactar objetivos del notebook

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-02

### Objetivo
Reemplazar placeholders con objetivos y preguntas; separar 4,5 externo de rating.

### Requisitos relacionados
- REQ-OBJ-001
- REQ-OBJ-002
- REQ-OBJ-003
- REQ-NOTEBOOK-001
- REQ-NOTEBOOK-002
- NFR-006

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-001

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Reemplazar placeholders con objetivos y preguntas; separar 4,5 externo de rating.
3. Ejecutar TEST-WLR-003 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Reemplazar placeholders con objetivos y preguntas; separar 4,5 externo de rating.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-003 aprobada.

### Verificación
TEST-WLR-003 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-004 — Explorar calidad y valoraciones

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-02

### Objetivo
Mostrar tipos, nulos, duplicados y distribución humana sin borrar filas.

### Requisitos relacionados
- REQ-EDA-001
- REQ-EDA-002
- REQ-EDA-003
- REQ-EDA-004
- REQ-EDA-005
- REQ-EDA-006
- REQ-NOTEBOOK-003

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-003

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Mostrar tipos, nulos, duplicados y distribución humana sin borrar filas.
3. Ejecutar TEST-WLR-004 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Mostrar tipos, nulos, duplicados y distribución humana sin borrar filas.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-004 aprobada.

### Verificación
TEST-WLR-004 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-005 — Explorar longitudes e insights

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-02

### Objetivo
Medir caracteres y palabras; identificar idiomas razonables y documentar insights con evidencia.

### Requisitos relacionados
- REQ-EDA-007
- REQ-EDA-008
- REQ-EDA-009

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-004

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Medir caracteres y palabras; identificar idiomas razonables y documentar insights con evidencia.
3. Ejecutar TEST-WLR-005 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Medir caracteres y palabras; identificar idiomas razonables y documentar insights con evidencia.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-005 aprobada.

### Verificación
TEST-WLR-005 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-006 — Definir limpieza y plan de acción

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-02

### Objetivo
Mantener texto original; definir estados, justificación de transformaciones y secuencia analítica.

### Requisitos relacionados
- REQ-CLEAN-001
- REQ-CLEAN-002
- REQ-CLEAN-003
- REQ-CLEAN-004
- REQ-CLEAN-005
- REQ-CLEAN-006
- REQ-CLEAN-007
- REQ-NOTEBOOK-004
- REQ-NOTEBOOK-005

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-005

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Mantener texto original; definir estados, justificación de transformaciones y secuencia analítica.
3. Ejecutar TEST-WLR-006 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Mantener texto original; definir estados, justificación de transformaciones y secuencia analítica.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-006 aprobada.

### Verificación
TEST-WLR-006 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** CSV original validado y notebook ejecutado con tablas EDA. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-007 — Integrar carga única del modelo

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-03

### Objetivo
Inicializar pipeline y tokenizer una sola vez en CPU, revisión fijada y evaluación; documentar dominio.

### Requisitos relacionados
- REQ-MODEL-001
- REQ-MODEL-002
- REQ-MODEL-003
- REQ-MODEL-004
- REQ-MODEL-005
- REQ-MODEL-008
- REQ-NOTEBOOK-006
- NFR-004

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-002
- TASK-WLR-006

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Inicializar pipeline y tokenizer una sola vez en CPU, revisión fijada y evaluación; documentar dominio.
3. Ejecutar TEST-WLR-007 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Inicializar pipeline y tokenizer una sola vez en CPU, revisión fijada y evaluación; documentar dominio.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-007 aprobada.

### Verificación
TEST-WLR-007 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-008 — Validar etiquetas y sentimiento

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-03

### Objetivo
Definir diccionarios exactos de etiquetas y bandas; comprobar cinco valores y entradas inválidas.

### Requisitos relacionados
- REQ-MODEL-006
- REQ-SENT-001
- REQ-SENT-002
- REQ-SENT-003
- REQ-SENT-004
- REQ-SENT-005

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-007

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Definir diccionarios exactos de etiquetas y bandas; comprobar cinco valores y entradas inválidas.
3. Ejecutar TEST-WLR-008 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Definir diccionarios exactos de etiquetas y bandas; comprobar cinco valores y entradas inválidas.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-008 aprobada.

### Verificación
TEST-WLR-008 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-009 — Medir tokens y truncamiento

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-03

### Objetivo
Contar tokens sin truncar; registrar IDs que superen 512 incluyendo especiales y política de truncamiento.

### Requisitos relacionados
- REQ-EDA-007
- REQ-CLEAN-006
- REQ-MODEL-008

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-007

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Contar tokens sin truncar; registrar IDs que superen 512 incluyendo especiales y política de truncamiento.
3. Ejecutar TEST-WLR-009 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Contar tokens sin truncar; registrar IDs que superen 512 incluyendo especiales y política de truncamiento.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-009 aprobada.

### Verificación
TEST-WLR-009 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-010 — Ejecutar inferencia y evaluar lotes

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-03

### Objetivo
Comparar lote 8 frente a 1 sobre muestra fija; conservar clases iguales; inferir todas las filas y registrar fallos.

### Requisitos relacionados
- REQ-MODEL-004
- REQ-MODEL-005
- REQ-MODEL-006
- REQ-MODEL-007
- REQ-MODEL-009
- REQ-CLEAN-007
- REQ-SENT-003
- REQ-SENT-004

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-008
- TASK-WLR-009

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Comparar lote 8 frente a 1 sobre muestra fija; conservar clases iguales; inferir todas las filas y registrar fallos.
3. Ejecutar TEST-WLR-010 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Comparar lote 8 frente a 1 sobre muestra fija; conservar clases iguales; inferir todas las filas y registrar fallos.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-010 aprobada.

### Verificación
TEST-WLR-010 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-011 — Calcular distribuciones y media

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-04

### Objetivo
Calcular conteos, porcentajes y media usando denominador explícito de predicciones válidas.

### Requisitos relacionados
- REQ-ANALYSIS-001
- REQ-ANALYSIS-002
- REQ-ANALYSIS-003
- REQ-ANALYSIS-004
- REQ-ANALYSIS-005
- REQ-NOTEBOOK-007

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-010

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Calcular conteos, porcentajes y media usando denominador explícito de predicciones válidas.
3. Ejecutar TEST-WLR-011 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Calcular conteos, porcentajes y media usando denominador explícito de predicciones válidas.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-011 aprobada.

### Verificación
TEST-WLR-011 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-012 — Comparar referencia y discrepancias

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-04

### Objetivo
Comparar media con 4,5 y con rating muestral; tabla por ID y diferencia predicha menos humana.

### Requisitos relacionados
- REQ-ANALYSIS-006
- REQ-ANALYSIS-007
- REQ-ANALYSIS-008
- REQ-ANALYSIS-009

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-011

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Comparar media con 4,5 y con rating muestral; tabla por ID y diferencia predicha menos humana.
3. Ejecutar TEST-WLR-012 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Comparar media con 4,5 y con rating muestral; tabla por ID y diferencia predicha menos humana.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-012 aprobada.

### Verificación
TEST-WLR-012 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-013 — Analizar candidatos a falsos negativos

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-04

### Objetivo
Filtrar 1–2 frente a 4–5; documentar ejemplos reales, hipótesis y ausencia de candidatos si procede.

### Requisitos relacionados
- REQ-FN-001
- REQ-FN-003
- REQ-FN-004
- REQ-FN-005
- REQ-FN-006
- REQ-NOTEBOOK-008

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-012

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Filtrar 1–2 frente a 4–5; documentar ejemplos reales, hipótesis y ausencia de candidatos si procede.
3. Ejecutar TEST-WLR-013 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Filtrar 1–2 frente a 4–5; documentar ejemplos reales, hipótesis y ausencia de candidatos si procede.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-013 aprobada.

### Verificación
TEST-WLR-013 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Aclaración incremental:** esta tarea identifica candidatos y patrones; la confirmación textual real de REQ-FN-002/007 pertenece a TASK-WLR-015. Se evita exigir la revisión antes de seleccionar la muestra.

**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-014 — Seleccionar muestra manual

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-05

### Objetivo
Seleccionar 18 IDs sin reemplazo con semilla 42, estratos disponibles y discrepancias; explicar cuotas.

### Requisitos relacionados
- REQ-VALID-001
- REQ-VALID-002
- REQ-VALID-003
- REQ-VALID-004
- REQ-VALID-005
- REQ-VALID-008

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-013

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Seleccionar 18 IDs sin reemplazo con semilla 42, estratos disponibles y discrepancias; explicar cuotas.
3. Ejecutar TEST-WLR-014 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Seleccionar 18 IDs sin reemplazo con semilla 42, estratos disponibles y discrepancias; explicar cuotas.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-014 aprobada.

### Verificación
TEST-WLR-014 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** Notebook ejecutado desde kernel limpio; etiquetas, tokens, lotes y resultados reales verificados. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-015 — Realizar revisión humana

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-05

### Objetivo
Solicitar lectura real de 18 textos al revisor, registrar autor/fecha, etiqueta manual y razones; no inventar anotaciones.

### Requisitos relacionados
- REQ-VALID-006
- REQ-VALID-007
- REQ-FN-002
- REQ-FN-007
- REQ-NOTEBOOK-009

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-014

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Solicitar lectura real de 18 textos al revisor, registrar autor/fecha, etiqueta manual y razones; no inventar anotaciones.
3. Ejecutar TEST-WLR-015 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Solicitar lectura real de 18 textos al revisor, registrar autor/fecha, etiqueta manual y razones; no inventar anotaciones.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-015 aprobada.

### Verificación
TEST-WLR-015 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia final (2026-11-06):** usuario confirma revisión lista; 18 anotaciones de ark verificadas, notebook reejecutado sin errores y predicciones del CSV idénticas. Conclusiones integran 13 acuerdos, 5 discrepancias y 3 falsos negativos revisados, sin extrapolar precisión poblacional.
## TASK-WLR-016 — Redactar conclusiones de negocio

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-05

### Objetivo
Responder preguntas, presentar cifras reales y límites de muestra y dominio para account manager.

### Requisitos relacionados
- REQ-ANALYSIS-009
- REQ-NOTEBOOK-010
- REQ-NOTEBOOK-011
- NFR-006

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-015

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Responder preguntas, presentar cifras reales y límites de muestra y dominio para account manager.
3. Ejecutar TEST-WLR-016 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Responder preguntas, presentar cifras reales y límites de muestra y dominio para account manager.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-016 aprobada.

### Verificación
TEST-WLR-016 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia final (2026-11-06):** usuario confirma revisión lista; 18 anotaciones de ark verificadas, notebook reejecutado sin errores y predicciones del CSV idénticas. Conclusiones integran 13 acuerdos, 5 discrepancias y 3 falsos negativos revisados, sin extrapolar precisión poblacional.
## TASK-WLR-017 — Extraer carga y validación al script

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-06

### Objetivo
Sustituir arranque db_connect por main con carga/validación; resolver rutas mediante __file__; no tocar utils.

### Requisitos relacionados
- REQ-PROD-001
- REQ-PROD-002
- REQ-PROD-007
- REQ-PROD-009
- NFR-005
- NFR-007
- NFR-008

### Archivos afectados
- `src/app.py`

### Dependencias
- TASK-WLR-010

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Sustituir arranque db_connect por main con carga/validación; resolver rutas mediante __file__; no tocar utils.
3. Ejecutar TEST-WLR-017 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Sustituir arranque db_connect por main con carga/validación; resolver rutas mediante __file__; no tocar utils.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-017 aprobada.

### Verificación
TEST-WLR-017 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/app.py`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** app.py ejecutado con 500 filas ok, CSV releído e íntegro; 10 tests unittest aprobados, pip check correcto y ejecución offline desde /private/tmp. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-018 — Extraer inferencia reproducible

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-06

### Objetivo
Extraer funciones de modelo y mapeo; notebook reutiliza funciones sin ejecutar main; conservar configuración.

### Requisitos relacionados
- REQ-PROD-003
- REQ-PROD-004
- REQ-PROD-005
- REQ-PROD-006
- REQ-MODEL-003
- REQ-MODEL-004
- REQ-MODEL-005
- REQ-MODEL-006
- REQ-MODEL-007
- REQ-MODEL-009
- REQ-SENT-001
- REQ-SENT-002
- REQ-SENT-003
- REQ-SENT-004
- REQ-SENT-005
- NFR-001
- NFR-002
- NFR-003
- NFR-004

### Archivos afectados
- `src/app.py`
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-017
- TASK-WLR-008
- TASK-WLR-009

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Extraer funciones de modelo y mapeo; notebook reutiliza funciones sin ejecutar main; conservar configuración.
3. Ejecutar TEST-WLR-018 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Extraer funciones de modelo y mapeo; notebook reutiliza funciones sin ejecutar main; conservar configuración.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-018 aprobada.

### Verificación
TEST-WLR-018 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/app.py`, `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** app.py ejecutado con 500 filas ok, CSV releído e íntegro; 10 tests unittest aprobados, pip check correcto y ejecución offline desde /private/tmp. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-019 — Exportar y verificar CSV

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-06

### Objetivo
Escribir CSV sin índice vía archivo temporal en processed; releer y comparar IDs/textos/valores; fallos visibles.

### Requisitos relacionados
- REQ-PROD-007
- REQ-PROD-008
- REQ-PROD-009
- REQ-CLEAN-005
- REQ-CLEAN-007
- NFR-002
- NFR-003
- NFR-008

### Archivos afectados
- `src/app.py`
- `data/processed/reviews_with_sentiment.csv`

### Dependencias
- TASK-WLR-018

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Escribir CSV sin índice vía archivo temporal en processed; releer y comparar IDs/textos/valores; fallos visibles.
3. Ejecutar TEST-WLR-019 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Escribir CSV sin índice vía archivo temporal en processed; releer y comparar IDs/textos/valores; fallos visibles.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-019 aprobada.

### Verificación
TEST-WLR-019 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/app.py`, `data/processed/reviews_with_sentiment.csv`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** app.py ejecutado con 500 filas ok, CSV releído e íntegro; 10 tests unittest aprobados, pip check correcto y ejecución offline desde /private/tmp. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-020 — Verificar ruta de producción

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-07

### Objetivo
Comprobar casos críticos con unittest/mocks y ejecutar script real; pip check y comparación por ID.

### Requisitos relacionados
- REQ-PROD-001
- REQ-PROD-002
- REQ-PROD-003
- REQ-PROD-004
- REQ-PROD-005
- REQ-PROD-006
- REQ-PROD-007
- REQ-PROD-008
- REQ-PROD-009
- REQ-PROD-010
- REQ-MODEL-001
- REQ-MODEL-002
- REQ-MODEL-003
- REQ-MODEL-004
- REQ-MODEL-005
- REQ-MODEL-006
- REQ-MODEL-007
- REQ-MODEL-008
- REQ-MODEL-009
- REQ-SENT-001
- REQ-SENT-002
- REQ-SENT-003
- REQ-SENT-004
- REQ-SENT-005
- NFR-001
- NFR-002
- NFR-003
- NFR-004
- NFR-005
- NFR-007
- NFR-008
- NFR-009

### Archivos afectados
- `tests/test_app.py (propuesto)`
- `src/app.py`
- `data/processed/reviews_with_sentiment.csv`

### Dependencias
- TASK-WLR-019

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Comprobar casos críticos con unittest/mocks y ejecutar script real; pip check y comparación por ID.
3. Ejecutar TEST-WLR-020 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Comprobar casos críticos con unittest/mocks y ejecutar script real; pip check y comparación por ID.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-020 aprobada.

### Verificación
TEST-WLR-020 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `tests/test_app.py (propuesto)`, `src/app.py`, `data/processed/reviews_with_sentiment.csv`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia obtenida (2026-11-06):** app.py ejecutado con 500 filas ok, CSV releído e íntegro; 10 tests unittest aprobados, pip check correcto y ejecución offline desde /private/tmp. Ver src/explore.ipynb y data/processed/execution_metadata.json.
## TASK-WLR-021 — Ejecutar notebook completo

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-07

### Objetivo
Reiniciar kernel, ejecutar todas las celdas; confirmar salidas reales, gráficos legibles y revisión humana preservada.

### Requisitos relacionados
- REQ-NOTEBOOK-001
- REQ-NOTEBOOK-002
- REQ-NOTEBOOK-003
- REQ-NOTEBOOK-004
- REQ-NOTEBOOK-005
- REQ-NOTEBOOK-006
- REQ-NOTEBOOK-007
- REQ-NOTEBOOK-008
- REQ-NOTEBOOK-009
- REQ-NOTEBOOK-010
- REQ-NOTEBOOK-011
- REQ-NOTEBOOK-012
- REQ-ANALYSIS-001
- REQ-ANALYSIS-002
- REQ-ANALYSIS-003
- REQ-ANALYSIS-004
- REQ-ANALYSIS-005
- REQ-ANALYSIS-006
- REQ-ANALYSIS-007
- REQ-ANALYSIS-008
- REQ-ANALYSIS-009
- REQ-VALID-001
- REQ-VALID-002
- REQ-VALID-003
- REQ-VALID-004
- REQ-VALID-005
- REQ-VALID-006
- REQ-VALID-007
- REQ-VALID-008
- NFR-006

### Archivos afectados
- `src/explore.ipynb`

### Dependencias
- TASK-WLR-016
- TASK-WLR-020

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Reiniciar kernel, ejecutar todas las celdas; confirmar salidas reales, gráficos legibles y revisión humana preservada.
3. Ejecutar TEST-WLR-021 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Reiniciar kernel, ejecutar todas las celdas; confirmar salidas reales, gráficos legibles y revisión humana preservada.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-021 aprobada.

### Verificación
TEST-WLR-021 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.


**Evidencia final (2026-11-06):** usuario confirma revisión lista; 18 anotaciones de ark verificadas, notebook reejecutado sin errores y predicciones del CSV idénticas. Conclusiones integran 13 acuerdos, 5 discrepancias y 3 falsos negativos revisados, sin extrapolar precisión poblacional.
## TASK-WLR-022 — Auditar entrega y aceptación

**Estado:** Completed
**Prioridad:** High
**Fase:** PLAN-07

### Objetivo
Contrastar checklist, hashes y trazabilidad; preparar artefactos para GitHub sin commit ni push automático.

### Requisitos relacionados
- REQ-OBJ-001
- REQ-OBJ-002
- REQ-OBJ-003
- REQ-EDA-001
- REQ-EDA-002
- REQ-EDA-003
- REQ-EDA-004
- REQ-EDA-005
- REQ-EDA-006
- REQ-EDA-007
- REQ-EDA-008
- REQ-EDA-009
- REQ-CLEAN-001
- REQ-CLEAN-002
- REQ-CLEAN-003
- REQ-CLEAN-004
- REQ-CLEAN-005
- REQ-CLEAN-006
- REQ-CLEAN-007
- REQ-MODEL-001
- REQ-MODEL-002
- REQ-MODEL-003
- REQ-MODEL-004
- REQ-MODEL-005
- REQ-MODEL-006
- REQ-MODEL-007
- REQ-MODEL-008
- REQ-MODEL-009
- REQ-SENT-001
- REQ-SENT-002
- REQ-SENT-003
- REQ-SENT-004
- REQ-SENT-005
- REQ-ANALYSIS-001
- REQ-ANALYSIS-002
- REQ-ANALYSIS-003
- REQ-ANALYSIS-004
- REQ-ANALYSIS-005
- REQ-ANALYSIS-006
- REQ-ANALYSIS-007
- REQ-ANALYSIS-008
- REQ-ANALYSIS-009
- REQ-FN-001
- REQ-FN-002
- REQ-FN-003
- REQ-FN-004
- REQ-FN-005
- REQ-FN-006
- REQ-FN-007
- REQ-VALID-001
- REQ-VALID-002
- REQ-VALID-003
- REQ-VALID-004
- REQ-VALID-005
- REQ-VALID-006
- REQ-VALID-007
- REQ-VALID-008
- REQ-NOTEBOOK-001
- REQ-NOTEBOOK-002
- REQ-NOTEBOOK-003
- REQ-NOTEBOOK-004
- REQ-NOTEBOOK-005
- REQ-NOTEBOOK-006
- REQ-NOTEBOOK-007
- REQ-NOTEBOOK-008
- REQ-NOTEBOOK-009
- REQ-NOTEBOOK-010
- REQ-NOTEBOOK-011
- REQ-NOTEBOOK-012
- REQ-PROD-001
- REQ-PROD-002
- REQ-PROD-003
- REQ-PROD-004
- REQ-PROD-005
- REQ-PROD-006
- REQ-PROD-007
- REQ-PROD-008
- REQ-PROD-009
- REQ-PROD-010
- NFR-001
- NFR-002
- NFR-003
- NFR-004
- NFR-005
- NFR-006
- NFR-007
- NFR-008
- NFR-009

### Archivos afectados
- `src/explore.ipynb`
- `src/app.py`
- `requirements.txt`
- `data/processed/reviews_with_sentiment.csv`

### Dependencias
- TASK-WLR-021

### Acciones
1. Comprobar entradas y condiciones de design.md.
2. Contrastar checklist, hashes y trazabilidad; preparar artefactos para GitHub sin commit ni push automático.
3. Ejecutar TEST-WLR-022 y guardar evidencia en el notebook o artefacto indicado, fuera de memory-bank.

### Criterios de aceptación
- [x] Contrastar checklist, hashes y trazabilidad; preparar artefactos para GitHub sin commit ni push automático.
- [x] Requisitos relacionados satisfechos y comprobación TEST-WLR-022 aprobada.

### Verificación
TEST-WLR-022 de testing-strategy.md; confirmar por review_id cuando intervengan filas.

### Evidencia
Salidas reales y/o inspección de `src/explore.ipynb`, `src/app.py`, `requirements.txt`, `data/processed/reviews_with_sentiment.csv`; registrar resultado, configuración y limitaciones.

### Restricciones
No entrenar, cambiar modelo, alterar CSV original, descartar filas silenciosamente, inventar anotaciones, versionar pesos ni realizar commits/pushes automáticos.

**Evidencia final (2026-11-06):** usuario confirma revisión lista; 18 anotaciones de ark verificadas, notebook reejecutado sin errores y predicciones del CSV idénticas. Conclusiones integran 13 acuerdos, 5 discrepancias y 3 falsos negativos revisados, sin extrapolar precisión poblacional.
