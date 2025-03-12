from typing import Dict, List, Optional

from libs.common.domain.entity.entity1 import Entity1
from libs.common.domain.repository.repository1 import Repository1


class InMemoryRepository1(Repository1):
    def __init__(self) -> None:
        self._entities: Dict[str, Entity1] = {}

    async def get_by_id(self, entity_id: str) -> Optional[Entity1]:
        return self._entities.get(entity_id)

    async def get_all(self) -> List[Entity1]:
        return list(self._entities.values())

    async def create(self, entity: Entity1) -> Entity1:
        self._entities[entity.id] = entity
        return entity

    async def update(self, entity: Entity1) -> Optional[Entity1]:
        if entity.id not in self._entities:
            return None
        self._entities[entity.id] = entity
        return entity

    async def delete(self, entity_id: str) -> bool:
        if entity_id not in self._entities:
            return False
        del self._entities[entity_id]
        return True
