from typing import List


def snake_to_camel(snake_str: str) -> str:
    """スネークケースをキャメルケースに変換します"""
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def split_by_delimiter(text: str, delimiter: str = ",") -> List[str]:
    """文字列を区切り文字で分割してリストを返します"""
    if not text:
        return []
    return [item.strip() for item in text.split(delimiter)]
