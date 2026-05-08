import pandas as pd
import numpy as np


# ======================================================
# FUNCIONES GENERALES
# ======================================================

def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas duplicadas del DataFrame."""

    df = df.copy()
    df = df.drop_duplicates()

    return df


def limpiar_texto(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """Limpia espacios, caracteres corruptos y normaliza texto."""

    df = df.copy()

    for col in columnas:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.encode("utf-8", errors="ignore")
                .str.decode("utf-8", errors="ignore")
                .str.strip()
                .str.lower()
            )

            df[col] = df[col].replace(
                {
                    "nan": np.nan,
                    "none": np.nan,
                    "": np.nan,
                }
            )

    return df


def convertir_fechas(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """Convierte columnas de texto a formato fecha."""

    df = df.copy()

    for col in columnas:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce",
                dayfirst=True,
            )

    return df


def tratar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """Imputa valores nulos en columnas numéricas y categóricas."""

    df = df.copy()

    columnas_numericas = df.select_dtypes(
        include=[np.number]
    ).columns

    columnas_texto = df.select_dtypes(
        include=["object"]
    ).columns

    for col in columnas_numericas:
        mediana = df[col].median()
        df[col] = df[col].fillna(mediana)

    for col in columnas_texto:
        moda = df[col].mode()

        if not moda.empty:
            df[col] = df[col].fillna(moda[0])
        else:
            df[col] = df[col].fillna("desconocido")

    return df


def limpiar_numero_desde_texto(serie: pd.Series) -> pd.Series:
    """Convierte valores numéricos almacenados como texto a float."""

    serie_limpia = (
        serie
        .astype(str)
        .str.encode("utf-8", errors="ignore")
        .str.decode("utf-8", errors="ignore")
        .str.replace(r"[^0-9.-]", "", regex=True)
    )

    return pd.to_numeric(serie_limpia, errors="coerce")


# ======================================================
# LIMPIEZA ESPECÍFICA POR DATASET
# ======================================================

def limpiar_envios(
    envios: pd.DataFrame,
    columnas_fecha: list,
    columnas_texto: list,
) -> pd.DataFrame:
    """Limpia el dataset de envíos."""

    envios = envios.copy()

    envios = eliminar_duplicados(envios)
    envios = limpiar_texto(envios, columnas_texto)
    envios = convertir_fechas(envios, columnas_fecha)

    if "peso_kg" in envios.columns:
        envios["peso_kg"] = limpiar_numero_desde_texto(envios["peso_kg"])

    envios = tratar_nulos(envios)

    return envios


def limpiar_rutas(
    rutas: pd.DataFrame,
    columnas_texto: list,
) -> pd.DataFrame:
    """Limpia el dataset de rutas."""

    rutas = rutas.copy()

    rutas = eliminar_duplicados(rutas)
    rutas = limpiar_texto(rutas, columnas_texto)
    rutas = tratar_nulos(rutas)

    return rutas


def limpiar_vehiculos(
    vehiculos: pd.DataFrame,
    columnas_texto: list,
) -> pd.DataFrame:
    """Limpia el dataset de vehículos."""

    vehiculos = vehiculos.copy()

    vehiculos = eliminar_duplicados(vehiculos)
    vehiculos = limpiar_texto(vehiculos, columnas_texto)
    vehiculos = tratar_nulos(vehiculos)

    return vehiculos


def limpiar_incidencias(
    incidencias: pd.DataFrame,
    columnas_fecha: list,
    columnas_texto: list,
) -> pd.DataFrame:
    """Limpia el dataset de incidencias."""

    incidencias = incidencias.copy()

    incidencias = eliminar_duplicados(incidencias)
    incidencias = limpiar_texto(incidencias, columnas_texto)
    incidencias = convertir_fechas(incidencias, columnas_fecha)

    if "costo_impacto" in incidencias.columns:
        incidencias["costo_impacto"] = limpiar_numero_desde_texto(
            incidencias["costo_impacto"]
        )

    incidencias = tratar_nulos(incidencias)

    return incidencias