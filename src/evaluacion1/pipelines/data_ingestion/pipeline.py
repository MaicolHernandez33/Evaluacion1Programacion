from kedro.pipeline import Pipeline, node
from .nodes import explorar_envios

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=explorar_envios,
            inputs="envios",
            outputs="envios_raw_checked",
            name="explorar_envios_node"
        )
    ])