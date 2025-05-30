import logging
import pandas as pd
from zenml import step
from sklearn.base import ClassifierMixin
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, roc_auc_score)


class Evaluator:
    pass


@step
def evaluate_model(X_test:pd.DataFrame, y_test:pd.Series, model:ClassifierMixin) -> dict:
    """Evaluates model performaces.
    
    Returns:
        dict: the performance scores.
    """
    pass