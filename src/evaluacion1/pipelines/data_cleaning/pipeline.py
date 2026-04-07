from kedro.pipeline import Pipeline, node
from .nodes import limpiar_envios

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=limpiar_envios,
            inputs="envios",
            outputs="envios_clean",
            name="limpiar_envios_node"
        )
    ])