import os
from typing import List


def get_app_path() -> str:
    """アプリケーションのルートパスを取得します"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))


def list_directories(path: str) -> List[str]:
    """指定されたパスにあるディレクトリのリストを返します"""
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
