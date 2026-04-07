from kedro.pipeline import Pipeline, node
from .nodes import limpiar_envios, limpiar_rutas, limpiar_vehiculos
from .nodes import transformar_datos, validar_datos

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Limpieza
        node(
            func=limpiar_envios,
            inputs="envios",
            outputs="envios_clean",
            name="limpiar_envios_node"
        ),
        node(
            func=limpiar_rutas,
            inputs="rutas",
            outputs="rutas_clean",
            name="limpiar_rutas_node"
        ),
        node(
            func=limpiar_vehiculos,
            inputs="vehiculos",
            outputs="vehiculos_clean",
            name="limpiar_vehiculos_node"
        ),
        # Transformación
        node(
            func=transformar_datos,
            inputs=["envios_clean", "rutas_clean", "vehiculos_clean"],
            outputs="dataset_final",
            name="transformar_datos_node"
        ),
        # Validación
        node(
            func=validar_datos,
            inputs="dataset_final",
            outputs="dataset_final_validado",
            name="validar_datos_node"
        )
    ])