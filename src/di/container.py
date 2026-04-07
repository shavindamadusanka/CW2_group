from dependency_injector import containers, providers
from core.util import LoggerFactory, ILogger
from core.data.repository.local_file_repository import LocalFileRepository
from core.domain.usecases.data_io_usecase import LoadDataUseCase, SaveDataUseCase

class AppContainer(containers.DeclarativeContainer):
    """
    DI for the app
    """
    config = providers.Configuration()

    logger = providers.Singleton(
        LoggerFactory.create,
        logger_type="console",  # config.logger_type
        name="App"
    )

    data_repository = providers.Singleton(
        LocalFileRepository,
        logger=logger
    )

    load_data_usecase = providers.Factory(
        LoadDataUseCase,
        repository=data_repository,
        logger=logger
    )

    save_data_usecase = providers.Factory(
        SaveDataUseCase,
        repository=data_repository,
        logger=logger
    )
