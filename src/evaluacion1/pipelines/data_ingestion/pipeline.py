from kedro.pipeline import Pipeline, node, pipeline

from .nodes import generar_reporte_ingestion


def create_pipeline(**kwargs) -> Pipeline:
    """Crea el pipeline de ingesta de datos."""

    return pipeline(
        [
            node(
                func=generar_reporte_ingestion,
                inputs=["envios", "rutas", "vehiculos", "incidencias"],
                outputs="reporte_ingestion",
                name="generar_reporte_ingestion_node",
            )
        ]
    )