# app/common/domain/repository/repository1.py
from abc import ABC, abstractmethod
from typing import List, Optional

from libs.common.domain.entity.entity1 import Entity1


class Repository1(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str) -> Optional[Entity1]:
        pass

    @abstractmethod
    async def get_all(self) -> List[Entity1]:
        pass

    @abstractmethod
    async def create(self, entity: Entity1) -> Entity1:
        pass

    @abstractmethod
    async def update(self, entity: Entity1) -> Optional[Entity1]:
        pass

    @abstractmethod
    async def delete(self, entity_id: str) -> bool:
        pass
