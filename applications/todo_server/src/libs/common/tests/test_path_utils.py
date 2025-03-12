import os

from libs.common.utils.path_utils import get_app_path, list_directories


class TestPathUtils:
    def test_get_app_path(self):
        app_path = get_app_path()
        assert os.path.exists(app_path)
        assert os.path.isdir(app_path)

    def test_list_directories(self, tmp_path):
        # テスト用のディレクトリ構造を作成
        dir1 = tmp_path / "dir1"
        dir1.mkdir()
        dir2 = tmp_path / "dir2"
        dir2.mkdir()
        file1 = tmp_path / "file1.txt"
        file1.write_text("test content")

        # ディレクトリのリストを取得
        dirs = list_directories(str(tmp_path))

        # 結果の確認
        assert len(dirs) == 2
        assert "dir1" in dirs
        assert "dir2" in dirs
        assert "file1.txt" not in dirs
