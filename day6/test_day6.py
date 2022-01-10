import numpy as np
import pytest

from day6 import compute_number_of_lantern_fish, read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day6.csv")


def test_num_fish_after_18_days(dummy_data) -> None:
    """
    checks the number of fish as expected
    """
    days = 18
    expected = 26
    computed = compute_number_of_lantern_fish(dummy_data, days)
    assert computed == expected


def test_num_fish_after_80_days(dummy_data) -> None:
    """
    checks the number of fish as expected
    """
    days = 80
    expected = 5934
    computed = compute_number_of_lantern_fish(dummy_data, days)
    assert computed == expected
