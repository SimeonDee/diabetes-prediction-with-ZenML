import logging
import pandas as pd
from zenml import step
from sklearn.base import ClassifierMixin

class Deployer:

    def __init__(self, model: ClassifierMixin, evaluation_result: dict):
        self.model = model
    
    def deploy(self):
        # deployment codes here, based on evaluation_result scores
        pass


@step
def deploy_model(model:ClassifierMixin, evlaution_results:dict) -> bool:
    """Deploy trained model model."""
    pass