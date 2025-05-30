from zenml import pipeline
from src.steps.ingest_data import ingest_data
from src.steps.preprocess_data import preprocess_data
from src.steps.segment_data import segment_data
from src.steps.train_model import train_model
from src.steps.evaluate_model import ingest_data
from src.steps.deploy_model import deploy_model

@pipeline
def diabetes_training_pipeline():
    pass