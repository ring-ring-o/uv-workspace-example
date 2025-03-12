from libs.common.domain.entity.entity1 import Entity1


class TestEntity1:
    def test_entity_creation(self):
        # テスト用エンティティの作成
        entity = Entity1(
            id="1", name="Test Entity", description="This is a test entity"
        )

        # 属性の確認
        assert entity.id == "1"
        assert entity.name == "Test Entity"
        assert entity.description == "This is a test entity"
