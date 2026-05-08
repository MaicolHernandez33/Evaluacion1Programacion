# 🚚 Evaluación 1 - Proyecto Logístico con Kedro

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## 📌 Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un flujo completo de ingeniería y análisis de datos aplicado a un contexto logístico, utilizando la arquitectura de pipelines de Kedro.

El sistema permite:

- Ingestar datasets logísticos
- Limpiar y transformar datos
- Integrar múltiples fuentes
- Validar calidad de datos
- Generar un dataset final listo para Machine Learning

El proyecto forma parte de la Evaluación 1 y servirá como base para la Evaluación 2, enfocada en análisis avanzado y modelos predictivos.

---

# 🏗️ Arquitectura del Proyecto

El flujo implementado sigue la siguiente estructura:

```text
RAW DATA
   ↓
INGESTION
   ↓
CLEANING
   ↓
TRANSFORMATION
   ↓
VALIDATION
   ↓
MODEL DATASET
```

---

# 📂 Estructura de Carpetas

```text
conf/                     Configuración Kedro
data/                     Datos del proyecto
notebooks/                Análisis y notebooks
src/                      Código fuente de pipelines
```

---

# ⚙️ Pipelines Implementados

## ✅ Ingestion Pipeline
Carga de datasets originales y generación de reporte inicial.

### Funciones:
- Lectura de CSV
- Validación inicial
- Detección de nulos
- Detección de duplicados
- Generación de reporte JSON

---

## ✅ Cleaning Pipeline
Proceso de limpieza y normalización de datos.

### Funciones:
- Eliminación de duplicados
- Tratamiento de valores nulos
- Conversión de fechas
- Corrección de tipos de datos
- Limpieza de texto y caracteres especiales

---

## ✅ Transformation Pipeline
Integración y creación de variables derivadas.

### Funciones:
- Integración de datasets
- Creación de features logísticas
- Variables para Machine Learning

### Variables creadas:
- `dias_entrega`
- `entrega_tardia`
- `cantidad_incidencias`
- `tiene_incidencia`
- `uso_capacidad_kg`
- `velocidad_promedio_km_h`

---

## ✅ Validation Pipeline
Validación final del dataset procesado.

### Funciones:
- Validación de columnas obligatorias
- Verificación de duplicados
- Revisión de nulos
- Generación de reporte final

---

# 📊 Dataset Final

El dataset final generado corresponde a:

```text
data/05_model_input/dataset_modelo.csv
```

Este dataset se encuentra:
- limpio
- integrado
- validado
- preparado para análisis y Machine Learning

---

# 🧠 Tecnologías Utilizadas

- Python
- Kedro
- Pandas
- NumPy
- Jupyter Notebook
- Matplotlib
- Seaborn

---

# ▶️ Ejecución del Proyecto

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar todos los pipelines

```bash
kedro run
```

---

## Abrir notebooks conectados a Kedro

```bash
kedro jupyter notebook
```

---

# 📈 Próxima Etapa

La Evaluación 2 utilizará el dataset generado para:

- Análisis exploratorio avanzado
- Visualización de datos
- Modelos de clasificación
- Modelos de regresión
- Evaluación de métricas
- Optimización de modelos

---

# 👨‍💻 Integrantes

- Maicol Hernández
- Francis Moya

---

# 📚 Profesor

Giocrisrai Godoy Bonillo
 