import logging
import pandas as pd
from zenml import step
from typing import Tuple
from typing_extensions import Annotated
from sklearn.model_selection import train_test_split

class SegmentData:
    """Segments preprocessed data."""

    def __init__(self, test_ratio:float=0.2):
        self.test_ratio = test_ratio

    def segment_data(self, features:pd.DataFrame, label:pd.Series) -> Tuple[
        Annotated[pd.DataFrame, "X_train"],
        Annotated[pd.Series, "y_train"],
        Annotated[pd.DataFrame, "X_test"],
        Annotated[pd.Series, "y_test"],
    ]:
        """Segments preprocessed data.
    
        Args:
            features (pd.DataFrame): features
            label (pd.Series): target label
        
        Returns:
            Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]: Returns the splitted data (X_train, y_train, X_test, y_test)
        """

        X_train, X_test, y_train, y_test = train_test_split(test_size=self.test_ratio, random_state=40)
        return X_train, y_train, X_test, y_test