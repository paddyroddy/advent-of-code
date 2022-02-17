from collections import Counter
from pathlib import Path

import numpy as np
from utils_day10 import (
    check_if_line_corrupted,
    complete_the_lines_with_score,
    compute_error_score_from_chars,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> list[str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return content


def compute_total_syntax_error_score(
    data: list[str],
) -> tuple[int, list[tuple[str, list[str]]]]:
    """
    finds the corrupted data and then compute the score
    """
    checked_lines = list(map(check_if_line_corrupted, data))
    offending_chars = Counter(c[0] for c in checked_lines if c[0])
    score = compute_error_score_from_chars(offending_chars)
    print(f"Q1 score: {score}")
    return score, checked_lines


def compute_total_completion_score(
    checked_lines: tuple[int, list[tuple[str, list[str]]]]
) -> int:
    """
    find the incomplete data and compute the score of completing chars
    """
    stacks = checked_lines[1]
    incomplete_stacks = [c[1] for c in stacks if not c[0]]
    incomplete_scores = list(map(complete_the_lines_with_score, incomplete_stacks))
    score = np.median(incomplete_scores).astype(int)
    print(f"Q2 score: {score}")
    return score


if __name__ == "__main__":
    navigation = read_data("data_day10.txt")
    checked_lines = compute_total_syntax_error_score(navigation)
    compute_total_completion_score(checked_lines)
