from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    limpiar_envios,
    limpiar_rutas,
    limpiar_vehiculos,
    limpiar_incidencias,
)


def create_pipeline(**kwargs) -> Pipeline:
    """Pipeline de limpieza de datos."""

    return pipeline([

        # ==================================================
        # ENVIOS
        # ==================================================

        node(
            func=limpiar_envios,
            inputs=[
                "envios",
                "params:columnas_fecha_envios",
                "params:columnas_texto_envios"
            ],
            outputs="envios_clean",
            name="limpiar_envios_node",
        ),

        # ==================================================
        # RUTAS
        # ==================================================

        node(
            func=limpiar_rutas,
            inputs=[
                "rutas",
                "params:columnas_texto_rutas"
            ],
            outputs="rutas_clean",
            name="limpiar_rutas_node",
        ),

        # ==================================================
        # VEHICULOS
        # ==================================================

        node(
            func=limpiar_vehiculos,
            inputs=[
                "vehiculos",
                "params:columnas_texto_vehiculos"
            ],
            outputs="vehiculos_clean",
            name="limpiar_vehiculos_node",
        ),

        # ==================================================
        # INCIDENCIAS
        # ==================================================

        node(
            func=limpiar_incidencias,
            inputs=[
                "incidencias",
                "params:columnas_fecha_incidencias",
                "params:columnas_texto_incidencias"
            ],
            outputs="incidencias_clean",
            name="limpiar_incidencias_node",
        ),

    ])