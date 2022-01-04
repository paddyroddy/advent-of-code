import pandas as pd
import pytest

from day5 import (
    compute_how_many_points_overlap,
    compute_overlapping_points_with_diagonals,
    read_data,
)


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day5.txt")


def test_num_points_overlapping(dummy_data) -> None:
    """
    checks the number of points overlapped
    """
    expected = 5
    computed = compute_how_many_points_overlap(dummy_data)
    assert computed == expected


def test_num_points_with_diagonals(dummy_data) -> None:
    """
    checks the number of points overlapped with diagonals
    """
    expected = 12
    computed = compute_overlapping_points_with_diagonals(dummy_data)
    assert computed == expected
