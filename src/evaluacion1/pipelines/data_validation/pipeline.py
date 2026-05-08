from kedro.pipeline import Pipeline, node, pipeline

from .nodes import validar_dataset_modelo


def create_pipeline(**kwargs) -> Pipeline:
    """Pipeline de validación final de datos."""

    return pipeline(
        [
            node(
                func=validar_dataset_modelo,
                inputs=[
                    "dataset_modelo",
                    "params:columnas_obligatorias_dataset_final",
                ],
                outputs="reporte_validacion",
                name="validar_dataset_modelo_node",
            )
        ]
    )