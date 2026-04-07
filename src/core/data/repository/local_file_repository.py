import pandas as pd
from core.domain.repository.idata_repository import IDataRepository
from core.domain.model.dataset_model import DatasetModel
from core.util.logger import ILogger

class LocalFileRepository(IDataRepository):
    """
    Concrete implementation of IDataRepository using pandas
    to read and write local files.
    """
    def __init__(self, logger: ILogger):
        self.logger = logger

    def load_data(self, path: str, **kwargs) -> DatasetModel:
        self.logger.info(f"Loading dataset from: {path}")
        try:
            df = pd.read_csv(path, **kwargs)
            self.logger.info(f"Successfully loaded dataset. Shape: {df.shape}")
            return DatasetModel(data=df)
        except Exception as e:
            self.logger.error(f"Error loading dataset from {path}: {str(e)}")
            raise e

    def save_data(self, dataset: DatasetModel, path: str, **kwargs):
        self.logger.info(f"Saving dataset to: {path}")
        try:
            dataset.data.to_csv(path, index=False, **kwargs)
            self.logger.info(f"Successfully saved dataset. Shape: {dataset.data.shape}")
        except Exception as e:
            self.logger.error(f"Error saving dataset to {path}: {str(e)}")
            raise e
