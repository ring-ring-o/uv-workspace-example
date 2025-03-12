import re
from typing import Any, List, Optional

from .base_splitter import TextSplitter


class RecursiveCharacterTextSplitter(TextSplitter):
    """テキストを再帰的に文字で分割するクラス。

    異なる区切り文字を再帰的に試しながら、適切なものを見つけて分割します。
    """

    def __init__(
        self,
        separators: Optional[List[str]] = None,
        is_separator_regex: bool = False,
        **kwargs: Any,
    ) -> None:
        """TextSplitterの新しいインスタンスを作成します。

        Args:
            separators: 分割に使用する区切り文字のリスト（優先順位順）
            is_separator_regex: 区切り文字が正規表現かどうかのフラグ
            **kwargs: 親クラスに渡す追加パラメータ
        """
        super().__init__(**kwargs)  # 親クラスの初期化
        # デフォルトの区切り文字リスト: 段落区切り、改行、スペース、空文字（1文字ずつ）
        self._separators = separators or ["\n\n", "\n", " ", ""]
        self._is_separator_regex = is_separator_regex  # 区切り文字が正規表現かどうか

    def _split_text(self, text: str, separators: List[str]) -> List[str]:
        """テキストを分割してチャンクのリストを返します。

        Args:
            text: 分割するテキスト
            separators: 使用する区切り文字のリスト

        Returns:
            分割されたテキストチャンクのリスト
        """
        final_chunks = []  # 最終的なチャンクを格納するリスト
        # 適切な区切り文字を選択
        separator = separators[-1]  # デフォルトは最後の区切り文字（通常は空文字）
        new_separators = []  # 次の再帰呼び出しで使用する区切り文字リスト

        # テキスト内に存在する最初の区切り文字を選択
        for i, _s in enumerate(separators):
            _separator = _s if self._is_separator_regex else re.escape(_s)
            if _s == "":  # 空文字の場合は文字単位で分割
                separator = _s
                break
            if re.search(_separator, text):  # テキスト内に区切り文字が存在するか確認
                separator = _s
                new_separators = separators[
                    i + 1 :
                ]  # 次の再帰呼び出しではより細かい区切り文字を使用
                break

        # 選択した区切り文字でテキストを分割
        _separator = separator if self._is_separator_regex else re.escape(separator)
        splits = self._split_text_with_regex(text, _separator)

        # 分割したチャンクを結合または再分割する処理
        _good_splits = []  # チャンクサイズ内に収まる分割を格納
        for s in splits:
            if (
                self._length_function(s) < self._chunk_size
            ):  # チャンクサイズ内に収まる場合
                _good_splits.append(s)
            else:  # チャンクサイズを超える場合
                if _good_splits:
                    # 既に集めた適切なサイズのチャンクを結合して最終リストに追加
                    merged_text = self._merge_splits(_good_splits, _separator)
                    final_chunks.extend(merged_text)
                    _good_splits = []  # リセット

                # 大きすぎるチャンクを再帰的に分割
                other_info = self._split_text(s, new_separators)
                final_chunks.extend(other_info)

        # 残った適切なサイズのチャンクを処理
        if _good_splits:
            merged_text = self._merge_splits(_good_splits, _separator)
            final_chunks.extend(merged_text)

        return final_chunks

    def split_text(self, text: str) -> List[str]:
        """入力テキストを事前定義された区切り文字に基づいて小さなチャンクに分割します。

        Args:
            text: 分割する入力テキスト

        Returns:
            分割後のテキストチャンクのリスト
        """
        return self._split_text(text, self._separators)

    def _split_text_with_regex(text: str, separator: str) -> List[str]:
        """正規表現を使用してテキストを分割します。

        Args:
            text: 分割するテキスト
            separator: 使用する区切り文字（正規表現）

        Returns:
            分割されたテキストのリスト（空文字は除外）
        """
        # 区切り文字を使ってテキストを分割
        if separator:
            splits = re.split(separator, text)
        else:
            splits = list(text)  # 空文字の場合は1文字ずつ分割
        return [s for s in splits if s != ""]  # 空文字を除外
