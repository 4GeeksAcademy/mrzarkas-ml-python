> Fecha: 2026-11-06. Especificación inicial de 2026-11-06; diseño y plan aprobados por el usuario el 2026-11-06. Implementación autorizada (GATE-05 Passed).

# Contexto verificado

## Negocio y alcance

WeLoveReviews asesora a una account manager sobre si el sentimiento textual de 500 reseñas coincide con la valoración externa de 4,5/5. Destinatarios: account manager, cliente y evaluador académico. El notebook deberá responder porcentajes positivo/neutral/negativo, distribución y media predichas, comparación con 4,5, discrepancias con rating, posibles falsos negativos, patrones, límites productos/servicios y conclusiones comprensibles. No se presupone discrepancia ni que 4,5 implique 90 % positivo. La procedencia temporal y representatividad de la referencia externa no están verificadas.

Se excluyen entrenamiento, fine-tuning, modelo alternativo, API, frontend, nueva base de datos y sustitución del notebook por informe Markdown. Esta fase solo documenta; tampoco instala dependencias ni ejecuta inferencia.

## Repositorio

README.md y README.es.md describen el template genérico 4Geeks; learn.json apunta a machine-learning-python-template. No existen AGENTS.md aplicables en el repositorio ni sus ancestros, PROMPT.es.md, instrucciones específicas adicionales, tests ni memory-bank previo. El adjunto del usuario es fuente de requisitos; no está disponible una rúbrica externa adicional.

Estructura real: src/app.py, src/utils.py, src/explore.ipynb; data/raw/reviews.csv y .gitkeep; data/interim/.gitkeep; data/processed/.gitkeep; models/.gitkeep; requirements.txt; README.md, README.es.md, learn.json, preview.jpg; .devcontainer/{Dockerfile,devcontainer.json,docker-compose.yml}; .vscode/settings.json; .gitignore; .env.example.

Notebook: dos celdas placeholder, sin ejecuciones ni salidas. Metadata histórica Python 3.8.13, no prueba de entorno actual. app.py importa db_connect y conecta antes del placeholder; no hay inferencia. utils.py contiene conexión SQLAlchemy y dotenv; no debe ser necesaria para el análisis. Ninguna funcionalidad NLP implementada.

Python del comando python3 inspeccionado: 3.14.6. Dockerfile: imagen Python 3.13 sin patch/digest fijo. README solicita 3.11+. No equivalen a un entorno probado para ML. pandas, numpy, transformers, torch, jupyter, nbformat y pytest no están instalados en este intérprete. Sin entorno virtual localizado.

requirements.txt: ipyleaflet>=0.14.0, ipywidgets>=7.7.1, matplotlib>=3.7.0, numpy>=1.24.2, opencv-python>=4.1.2, pandas>=2.3.3, psycopg2-binary>=2.9.3, pymysql>=1.0.2, python-dotenv>=0.20.0, requests>=2.27.1, scikit-learn, seaborn>=0.12.2, sqlalchemy>=2.0.38, sympy>=1.10.1, xgboost. Faltan Transformers, PyTorch y herramienta de ejecución notebook explícita; versiones no fijadas. El devcontainer instala requirements y configura PostgreSQL heredado. No modificarlo innecesariamente ni introducir nuevas dependencias de BD.

Convenciones: notebook exploratorio y extracción a app.py; CSV raw/interim/processed. Sin formateador o suite de tests declarados. Git inicial: reviews.csv es un archivo no versionado del usuario; preservar. Herramientas usadas: shell, Python estándar/csv/json/hashlib, git, curl. Solo lectura de datos.

## Inspección inicial de datos (sin EDA completa)

CSV UTF-8 legible: 500 filas, 3 columnas: review_id, rating, review_text. csv.DictReader devuelve cadenas; validación léxica permite enteros en review_id y rating. Tipos pandas aún no ejecutados: se comprobarán en EDA. IDs 1–500, únicos; rating con valores 1–5. Ningún campo vacío o solo espacios; no implica ausencia de cualquier marcador semántico de nulo, que se revisará en EDA. Cero filas idénticas; 493 textos únicos, siete repeticiones adicionales de texto. No eliminar reseñas con IDs distintos.

Muestras de IDs 1, 100, 250, 400 y 500 están en inglés y hablan de Harbor House Café; no se certifica idioma de cada fila. Los IDs 250 y 400 contienen experiencias mixtas (espera/personal frente a comida favorable); no son errores de modelo demostrados. La repetición de frases sugiere revisar origen y representatividad; no prueba datos sintéticos. Valoraciones humanas disponibles en rating, pero no son anotaciones independientes del sentimiento textual.

SHA-256 original: 63439a1a8c48fe8cc479b0b621b151b8da2415c58522b1e6b111582eef6edf10.

EDA posterior deberá medir distribución y media rating, longitudes caracteres/palabras/tokens, marcadores de nulo, textos repetidos con ratings distintos, idiomas y calidad. No se ha calculado sentimiento, media predicha ni métricas de validación. La falta de pipeline y entorno compatible es trabajo planificado, no defecto de resultados existentes.
