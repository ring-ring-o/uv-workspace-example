import pytest
from libs.common.domain.entity.entity1 import Entity1
from libs.common.infrastructure.repository.repository1 import InMemoryRepository1


class TestInMemoryRepository1:
    @pytest.fixture
    async def repository(self):
        return InMemoryRepository1()

    @pytest.fixture
    def test_entity(self):
        return Entity1(id="1", name="Test Entity", description="This is a test entity")

    @pytest.mark.asyncio
    async def test_create(self, repository, test_entity):
        # エンティティの作成
        created = await repository.create(test_entity)

        # 作成されたエンティティの確認
        assert created == test_entity

        # リポジトリから取得して確認
        stored = await repository.get_by_id("1")
        assert stored == test_entity

    @pytest.mark.asyncio
    async def test_get_all(self, repository, test_entity):
        # エンティティを作成
        await repository.create(test_entity)

        # 別のエンティティも作成
        entity2 = Entity1(
            id="2", name="Another Entity", description="This is another test entity"
        )
        await repository.create(entity2)

        # 全てのエンティティを取得して確認
        all_entities = await repository.get_all()
        assert len(all_entities) == 2
        assert test_entity in all_entities
        assert entity2 in all_entities

    @pytest.mark.asyncio
    async def test_update(self, repository, test_entity):
        # エンティティを作成
        await repository.create(test_entity)

        # エンティティを更新
        updated_entity = Entity1(
            id="1", name="Updated Entity", description="This is an updated entity"
        )
        result = await repository.update(updated_entity)

        # 更新結果の確認
        assert result == updated_entity

        # リポジトリから取得して確認
        stored = await repository.get_by_id("1")
        assert stored == updated_entity
        assert stored.name == "Updated Entity"

    @pytest.mark.asyncio
    async def test_delete(self, repository, test_entity):
        # エンティティを作成
        await repository.create(test_entity)

        # エンティティを削除
        result = await repository.delete("1")
        assert result is True

        # 削除後の確認
        stored = await repository.get_by_id("1")
        assert stored is None
