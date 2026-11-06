> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Riesgos y decisiones

Probabilidades cualitativas, sin estimar rendimiento no medido.

| ID | Riesgo | Probabilidad | Impacto | Mitigación | Evidencia necesaria | Estado |
|---|---|---|---|---|---|---|
| RISK-WLR-001 | Desajuste productos/servicios | Media | Clasificaciones inadecuadas | Revisión de ejemplos mixtos y límites de dominio | Ejemplos reales y razones del revisor | Open |
| RISK-WLR-002 | Ambigüedad e ironía | Media | Interpretación discutible | Permitir Ambiguous y separar rating/texto | Revisión textual independiente | Open |
| RISK-WLR-003 | Textos largos | No determinada | Pérdida por truncamiento | Contar tokens y registrar IDs >512 | Tabla tokens y truncamientos | Open |
| RISK-WLR-004 | Datos incompletos | Baja en inspección actual | Filas sin predicción | Validar vacíos/estados sin descartar filas | Conteos de calidad y fallos | Open |
| RISK-WLR-005 | Ausencia futura de rating | Baja en entrada actual | No comparar humanos | Detener contrato actual; renegociar si cambia fuente | Validación de columnas | Open |
| RISK-WLR-006 | Descarga y caché | Media | Inferencia bloqueada | Descarga automática a caché externa y mensajes claros | Carga real y prueba offline con caché | Open |
| RISK-WLR-007 | Dependencias incompatibles | Alta hasta resolución | Fallo de entorno | Resolver y fijar versiones en TASK-WLR-002 | pip check e imports | Open |
| RISK-WLR-008 | Cambios modelo remoto | Baja con SHA fijo | Falta reproducibilidad | Fijar SHA en modelo y tokenizer | Config registrada y revisión verificada | Open |
| RISK-WLR-009 | Caracteres CSV | Media | Corrupción de texto | UTF-8, quoting y relectura semántica | Prueba acentos/comas/comillas/saltos | Open |
| RISK-WLR-010 | Muestra sesgada | Alta si dirigida | Validación poco representativa | Estratos y criterio reproducible; no extrapolar accuracy | IDs, semilla, cuotas y límites | Open |
| RISK-WLR-011 | Origen y representatividad | No determinada | Conclusiones exageradas | Declarar referencia externa y patrones repetidos sin atribuir origen | EDA de duplicados y límites | Open |
| RISK-WLR-012 | Revisión humana no disponible | No determinada | Validación incompleta | Reservar revisión real; no inventar anotaciones | Autor/fecha/razones en 18 filas | Open |

## Decisiones

| ID | Estado | Decisión y justificación | Alternativas |
|---|---|---|---|
| DEC-WLR-001 | Aprobada por mandato del usuario | Modelo obligatorio, sin entrenamiento; inferencia en notebook y app.py. | Otros modelos/API descartados por alcance. |
| DEC-WLR-002 | Aprobada por mandato del usuario | Mapeo 1–2 negativo,3 neutral,4–5 positivo; preservar originales. | Otros umbrales prohibidos. |
| DEC-WLR-003 | Aprobada con el plan | Pipeline PyTorch CPU, carga única, SHA verificado, max_length 512; reutilizar tokenizer. | Inferencia manual AutoModel añade complejidad. |
| DEC-WLR-004 | Aprobada con el plan | Conservar textos repetidos con IDs distintos y registrar estados de error. | Deduplicación eliminaría parte de las 500 reseñas. |
| DEC-WLR-005 | Aprobada con el plan | Bandas CSV Negative/Neutral/Positive; columnas según design.md. | Variantes españolas producirían inconsistencia con tests exigidos. |
| DEC-WLR-006 | Verificada tras aprobación | Resolver versiones exactas y Python compatible en TASK-WLR-002; preferencia 3.13. | Reutilizar 3.14.6 o metadata 3.8.13 sin comprobar wheels no es evidencia de compatibilidad. |
| DEC-WLR-007 | Aprobada con el plan | Lote 8 solo si clases equivalentes frente a 1; sin optimización adicional. | Lote 1 es fallback válido; GPU innecesaria. |
| DEC-WLR-008 | Aprobada con el plan | Muestra 18, semilla 42 y revisión humana real, Ambiguous permitido. | Rating como verdad textual o anotación inventada no validan falsos negativos. |
| DEC-WLR-009 | Aprobada por mandato del usuario | No implementación antes de aprobación expresa. | Ninguna excepción inferida. |

Diseño y plan aprobados; GATE-03 y GATE-05 Passed. La resolución de entorno es tarea técnica autorizable con el plan; revisión real completada por ark durante TASK-WLR-015. No hay bloqueo de SHA: ha sido verificado. No se pide aclaración sobre discrepancias todavía no observadas.

## Estado de riesgos observado

RISK-WLR-004: ningún texto vacío en esta entrada. RISK-WLR-003: ningún texto superó 512 tokens. RISK-WLR-006/007/008: mitigados en entorno local mediante caché externa, ejecución offline, dependencias fijadas y SHA exacto; otros entornos aún no probados. RISK-WLR-012: revisión humana completada según registro de cierre. No confundir mitigación local con eliminación de riesgos de dominio.

## Revisión humana realizada

RISK-WLR-012 mitigado: 18 revisiones completadas por ark, confirmadas por el usuario. RISK-WLR-002/010 permanecen como limitaciones: casos mixtos y muestra dirigida no permiten estimar precisión poblacional. No se reinterpretaron ni sobrescribieron anotaciones.
