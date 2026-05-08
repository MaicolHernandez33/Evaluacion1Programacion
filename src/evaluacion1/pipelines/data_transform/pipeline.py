from kedro.pipeline import Pipeline, node, pipeline

from .nodes import integrar_datasets, crear_features_modelo


def create_pipeline(**kwargs) -> Pipeline:
    """Pipeline de transformación e integración de datos."""

    return pipeline(
        [
            node(
                func=integrar_datasets,
                inputs=[
                    "envios_clean",
                    "rutas_clean",
                    "vehiculos_clean",
                    "incidencias_clean",
                ],
                outputs="dataset_integrado",
                name="integrar_datasets_node",
            ),
            node(
                func=crear_features_modelo,
                inputs="dataset_integrado",
                outputs="dataset_modelo",
                name="crear_features_modelo_node",
            ),
        ]
    )