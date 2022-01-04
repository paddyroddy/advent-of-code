import pandas as pd
import pytest

from day5 import compute_how_many_points_overlap, read_data


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day5.txt")


def test_num_points_overlapping(dummy_data) -> None:
    """
    checks the number of points overlapped
    """
    expected = 5
    computed = compute_how_many_points_overlap(*dummy_data)
    assert computed == expected
