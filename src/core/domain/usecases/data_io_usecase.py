from core.domain.repository.idata_repository import IDataRepository
from core.domain.model.dataset_model import DatasetModel
from core.util.logger import ILogger

class LoadDataUseCase:
    """
    Use case for loading data through IDataRepository.
    """
    def __init__(self, repository: IDataRepository, logger: ILogger):
        self.repository = repository
        self.logger = logger
        
    def execute(self, path: str, **kwargs) -> DatasetModel:
        self.logger.info("Executing LoadDataUseCase")
        return self.repository.load_data(path, **kwargs)

class SaveDataUseCase:
    """
    Use case for saving data through IDataRepository.
    """
    def __init__(self, repository: IDataRepository, logger: ILogger):
        self.repository = repository
        self.logger = logger
        
    def execute(self, dataset: DatasetModel, path: str, **kwargs):
        self.logger.info("Executing SaveDataUseCase")
        self.repository.save_data(dataset, path, **kwargs)
