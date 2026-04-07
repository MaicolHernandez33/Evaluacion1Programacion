from kedro.pipeline import Pipeline, node
from .nodes import limpiar_envios, limpiar_rutas, limpiar_vehiculos

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Nodo para limpiar envíos
        node(
            func=limpiar_envios,
            inputs="envios",
            outputs="envios_clean",
            name="limpiar_envios_node"
        ),
        # Nodo para limpiar rutas
        node(
            func=limpiar_rutas,
            inputs="rutas",
            outputs="rutas_clean",
            name="limpiar_rutas_node"
        ),
        # Nodo para limpiar vehículos
        node(
            func=limpiar_vehiculos,
            inputs="vehiculos",
            outputs="vehiculos_clean",
            name="limpiar_vehiculos_node"
        ),
    ])