def count_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict[str, int]:
    text_lower = text.lower()
    return {char: text_lower.count(char) for char in set(text_lower)}

def sort_by_count(data: dict[str, int]) -> list[dict[str,str|int]]:
    dicts: list[dict[str,str|int]] = [{"char": char, "num": num} for char, num in data.items()]
    dicts.sort(key=lambda x: x["num"], reverse=True)
    return dicts
