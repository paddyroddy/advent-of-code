from pathlib import Path

from utils_day10 import compute_score_from_chars, find_if_line_corrupted

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
    # find_if_line_corrupted(data[0])
    find_if_line_corrupted(data[2])
    score = compute_score_from_chars({"}": 1, "]": 2, ")": 3})
    print(f"Q1 score: {score}")
    return score


if __name__ == "__main__":
    navigation = read_data("dummy_day10.txt")
    compute_total_syntax_error_score(navigation)
