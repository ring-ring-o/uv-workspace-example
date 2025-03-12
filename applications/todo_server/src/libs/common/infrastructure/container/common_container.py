from dependency_injector import containers, providers
from libs.common.domain.repository.repository1 import Repository1
from libs.common.infrastructure.repository.repository1 import InMemoryRepository1


class CommonContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository1 = providers.Factory(InMemoryRepository1)

    # エクスポートするプロバイダー
    repository1_provider = providers.Provider(Repository1, instance=repository1)
