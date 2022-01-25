import numpy as np
import pytest
from day4 import (
    find_who_first_won_bingo_and_compute_score,
    find_who_last_won_bingo_and_compute_score,
    read_data,
)


@pytest.fixture
def dummy_data() -> tuple[list[int], np.ndarray]:
    return read_data("dummy_day4.txt")


def test_first_bingo_score_as_expected(dummy_data) -> None:
    """
    checks the bingo score is as expected
    """
    expected = 4512
    computed = find_who_first_won_bingo_and_compute_score(*dummy_data)
    assert computed == expected


def test_last_bingo_score_as_expected(dummy_data) -> None:
    """
    checks the bingo score is as expected
    """
    expected = 1924
    computed = find_who_last_won_bingo_and_compute_score(*dummy_data)
    assert computed == expected
