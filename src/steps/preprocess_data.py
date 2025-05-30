import logging
import pandas as pd
from typing import Tuple
from typing_extensions import Annotated
from zenml import step


class PreprocessData:
    """Preprocesses that dataset."""

    def __init__(self, df:pd.DataFrame):
        """Initialization.
        Args:
            df (pd.DataFrame): data to preprocess.
        """
        self.df = df

    def preprocess_data(self) -> Tuple[
        Annotated[pd.DataFrame, "features"],
        Annotated[pd.Series, "label"]
    ]:
        """Preprocesses data.

        Returns:
            Tuple[pd.DataFrame, pd.Series]: first element is features and second element the target label.
        """
        # preprocessing steps here

        features = self.df[self.df.columns[:-1]]
        target_label = self.df[-1]
        return features, target_label
    

@step
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses data.

    Args:
        df (pd.DataFrame): data to preprocess.
        
    Returns:
        pd.DataFrame: preprocessed data.
    """
    logging.info("Preprocessing the data...")
    data_preprocessor = PreprocessData(df=df)
    return data_preprocessor.preprocess_data()
