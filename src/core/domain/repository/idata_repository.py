from abc import ABC, abstractmethod
from core.domain.model.dataset_model import DatasetModel

class IDataRepository(ABC):
    @abstractmethod
    def load_data(self, path: str, **kwargs) -> DatasetModel:
        pass

    @abstractmethod
    def save_data(self, dataset: DatasetModel, path: str, **kwargs):
        pass
