import pandas as pd


def resumen_dataframe(df: pd.DataFrame, nombre: str) -> dict:
    """Genera un resumen inicial de calidad para un DataFrame."""

    return {
        "nombre_dataset": nombre,
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "columnas_lista": df.columns.tolist(),
        "duplicados": int(df.duplicated().sum()),
        "nulos_por_columna": df.isnull().sum().astype(int).to_dict(),
        "tipos_datos": df.dtypes.astype(str).to_dict(),
    }


def generar_reporte_ingestion(
    envios: pd.DataFrame,
    rutas: pd.DataFrame,
    vehiculos: pd.DataFrame,
    incidencias: pd.DataFrame,
) -> dict:
    """Genera un reporte inicial para los cuatro datasets del proyecto."""

    reporte = {
        "envios": resumen_dataframe(envios, "envios"),
        "rutas": resumen_dataframe(rutas, "rutas"),
        "vehiculos": resumen_dataframe(vehiculos, "vehiculos"),
        "incidencias": resumen_dataframe(incidencias, "incidencias"),
    }

    return reporte