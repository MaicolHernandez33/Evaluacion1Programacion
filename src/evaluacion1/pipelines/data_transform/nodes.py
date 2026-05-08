import pandas as pd


def preparar_incidencias(incidencias_clean: pd.DataFrame) -> pd.DataFrame:
    """Resume las incidencias por envío para integrarlas al dataset principal."""

    incidencias_resumen = (
        incidencias_clean
        .groupby("id_envio")
        .agg(
            cantidad_incidencias=("id_incidencia", "count"),
            costo_total_incidencias=("costo_impacto", "sum"),
            tipo_incidencia_principal=("tipo_incidencia", "first"),
        )
        .reset_index()
    )

    incidencias_resumen["tiene_incidencia"] = 1

    return incidencias_resumen


def integrar_datasets(
    envios_clean: pd.DataFrame,
    rutas_clean: pd.DataFrame,
    vehiculos_clean: pd.DataFrame,
    incidencias_clean: pd.DataFrame,
) -> pd.DataFrame:
    """Integra envíos, rutas, vehículos e incidencias en un solo dataset."""

    incidencias_resumen = preparar_incidencias(incidencias_clean)

    dataset = envios_clean.merge(
        rutas_clean,
        on="id_ruta",
        how="left"
    )

    dataset = dataset.merge(
        vehiculos_clean,
        on="id_vehiculo",
        how="left"
    )

    dataset = dataset.merge(
        incidencias_resumen,
        on="id_envio",
        how="left"
    )

    dataset["cantidad_incidencias"] = dataset["cantidad_incidencias"].fillna(0)
    dataset["costo_total_incidencias"] = dataset["costo_total_incidencias"].fillna(0)
    dataset["tiene_incidencia"] = dataset["tiene_incidencia"].fillna(0)
    dataset["tipo_incidencia_principal"] = dataset["tipo_incidencia_principal"].fillna("sin incidencia")

    return dataset


def crear_features_modelo(dataset_integrado: pd.DataFrame) -> pd.DataFrame:
    """Crea variables derivadas para análisis y modelado posterior."""

    dataset = dataset_integrado.copy()

    dataset["fecha_envio"] = pd.to_datetime(dataset["fecha_envio"], errors="coerce")
    dataset["fecha_entrega"] = pd.to_datetime(dataset["fecha_entrega"], errors="coerce")

    dataset["dias_entrega"] = (
        dataset["fecha_entrega"] - dataset["fecha_envio"]
    ).dt.days

    dataset["dias_entrega"] = dataset["dias_entrega"].fillna(
        dataset["dias_entrega"].median()
    )

    dataset["velocidad_promedio_km_h"] = (
        dataset["distancia_km"] / dataset["tiempo_estimado_hrs"]
    )

    dataset["velocidad_promedio_km_h"] = dataset["velocidad_promedio_km_h"].replace(
        [float("inf"), -float("inf")],
        0
    )

    dataset["velocidad_promedio_km_h"] = dataset["velocidad_promedio_km_h"].fillna(0)

    dataset["uso_capacidad_kg"] = (
        dataset["peso_kg"] / dataset["capacidad_kg"]
    )

    dataset["uso_capacidad_m3"] = (
        dataset["volumen_m3"] / dataset["capacidad_m3"]
    )

    dataset["uso_capacidad_kg"] = dataset["uso_capacidad_kg"].replace(
        [float("inf"), -float("inf")],
        0
    ).fillna(0)

    dataset["uso_capacidad_m3"] = dataset["uso_capacidad_m3"].replace(
        [float("inf"), -float("inf")],
        0
    ).fillna(0)

    dataset["entrega_tardia"] = (
        dataset["dias_entrega"] > dataset["tiempo_estimado_hrs"] / 24
    ).astype(int)

    return dataset