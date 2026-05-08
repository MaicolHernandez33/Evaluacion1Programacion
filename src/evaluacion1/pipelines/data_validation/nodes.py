import pandas as pd


def validar_dataset_modelo(
    dataset_modelo: pd.DataFrame,
    columnas_obligatorias: list
) -> dict:
    """Valida la calidad final del dataset modelo."""

    columnas_existentes = dataset_modelo.columns.tolist()

    columnas_faltantes = [
        col for col in columnas_obligatorias
        if col not in columnas_existentes
    ]

    reporte = {
        "filas_dataset_modelo": int(dataset_modelo.shape[0]),
        "columnas_dataset_modelo": int(dataset_modelo.shape[1]),

        "columnas_obligatorias_revisadas": columnas_obligatorias,
        "columnas_faltantes": columnas_faltantes,

        "duplicados_finales": int(dataset_modelo.duplicated().sum()),

        "nulos_por_columna": (
            dataset_modelo
            .isnull()
            .sum()
            .astype(int)
            .to_dict()
        ),

        "tipos_datos": (
            dataset_modelo
            .dtypes
            .astype(str)
            .to_dict()
        ),

        "validacion_general": "aprobada" if len(columnas_faltantes) == 0 else "revisar",
    }

    return reporte