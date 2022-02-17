from collections import Counter
from pathlib import Path

from utils_day10 import check_if_line_corrupted, compute_score_from_chars

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> list[str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return content


def compute_total_syntax_error_score(data: list[str]) -> int:
    """
    finds the corrupted data and then compute the score
    """
    offending_chars = Counter(c for c in map(check_if_line_corrupted, data) if c)
    score = compute_score_from_chars(offending_chars)
    print(f"Q1 score: {score}")
    return score


if __name__ == "__main__":
    navigation = read_data("data_day10.txt")
    compute_total_syntax_error_score(navigation)
