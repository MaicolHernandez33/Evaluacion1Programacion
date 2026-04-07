from evaluacion1.pipelines.data_ingestion.pipeline import create_pipeline as ingestion_pipeline
from evaluacion1.pipelines.data_cleaning.pipeline import create_pipeline as cleaning_pipeline

def register_pipelines():
    return {
        "__default__": ingestion_pipeline() + cleaning_pipeline(),
        "data_ingestion": ingestion_pipeline(),
        "data_cleaning": cleaning_pipeline(),
    }