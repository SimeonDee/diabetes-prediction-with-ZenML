import logging
import pandas as pd
from zenml import step


class IngestData:
    """Data ingestion class."""

    def __init__(self, data_path: str):
        """Initialization.
        Args:
            data_path (str): path to the dataset.
        """
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
        """Loads the dataset as dataframe.
        Returns:
            pd.DataFrame: the loaded dataset.
        """
        logging.info("ingesting data...")
        df = pd.read_csv(self.data_path)
        return df

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """Ingests data."""
    data_ingester = IngestData(data_path=data_path)
    return data_ingester.get_data()
