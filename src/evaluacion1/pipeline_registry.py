"""Registro de pipelines del proyecto Kedro."""

from kedro.pipeline import Pipeline

from evaluacion1.pipelines import (
    data_ingestion,
    data_cleaning,
    data_transform,
    data_validation,
)


def register_pipelines() -> dict[str, Pipeline]:
    """Registra todos los pipelines disponibles."""

    ingestion_pipeline = data_ingestion.create_pipeline()
    cleaning_pipeline = data_cleaning.create_pipeline()
    transform_pipeline = data_transform.create_pipeline()
    validation_pipeline = data_validation.create_pipeline()

    return {
        "ingestion": ingestion_pipeline,
        "cleaning": cleaning_pipeline,
        "transform": transform_pipeline,
        "validation": validation_pipeline,

        "__default__": (
            ingestion_pipeline
            + cleaning_pipeline
            + transform_pipeline
            + validation_pipeline
        ),
    }