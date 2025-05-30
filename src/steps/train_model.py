import logging
import pandas as pd
from zenml import step
from typing import Tuple
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import ClassifierMixin

class TrainRFModel:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, criterion='gini')

    def train_model(self, X_train: pd.DataFrame, y_train:pd.Series) -> ClassifierMixin:
        """Trains a Random Forest model.
        
        Args:
            X_train: Training features.
            y_train: Training labels.
        
        Returns:
            ClassifierMixin: A trained model.
        """
        self.model.fit(X_train, y_train)
        return self.model