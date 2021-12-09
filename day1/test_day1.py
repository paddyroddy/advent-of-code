import pandas as pd
import pytest

from day1 import find_largest_measurements, fine_largest_sums, read_data


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day1.csv")


def test_number_depth_increases(dummy_data) -> None:
    """
    checks that the number of times increased matches the expected
    """
    expected = 7
    computed = find_largest_measurements(dummy_data)
    assert computed == expected


def test_sliding_window(dummy_data) -> None:
    """
    checks that the sum of sliding window increases as expected
    """
    expected = 5
    computed = fine_largest_sums(dummy_data)
    assert computed == expected
