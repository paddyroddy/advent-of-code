import pytest
from day10 import (
    compute_total_completion_score,
    compute_total_syntax_error_score,
    read_data,
)


@pytest.fixture
def dummy_data() -> list[str]:
    return read_data("dummy_day10.txt")


@pytest.fixture
def syntax_error_score(dummy_data) -> tuple[int, list[tuple[str, list[str]]]]:
    return compute_total_syntax_error_score(dummy_data)


def test_corrupted_char_score(syntax_error_score) -> None:
    """
    checks if the computed corruption score is correct
    """
    expected = 26397
    assert syntax_error_score[0] == expected


def test_incomplete_char_score(syntax_error_score) -> None:
    """
    checks if the computed completion score is correct
    """
    expected = 288957
    computed = compute_total_completion_score(syntax_error_score)
    assert computed == expected
