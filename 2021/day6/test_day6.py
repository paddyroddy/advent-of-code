import numpy as np
import pytest
from day6 import (
    compute_number_of_lantern_fish,
    read_data,
    simplified_sum_of_lantern_fish,
)


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day6.csv")


@pytest.mark.parametrize("days,expected", [(18, 26), (80, 5934)])
def test_num_fish_after_18_days(dummy_data, days, expected) -> None:
    """
    checks the number of fish as expected
    """
    computed = compute_number_of_lantern_fish(dummy_data, days)
    assert computed == expected


def test_simplified_sum_after_256_days(dummy_data) -> None:
    """
    checks the number of fish as expected
    """
    days = 256
    expected = 26984457539
    computed = simplified_sum_of_lantern_fish(dummy_data, days)
    assert computed == expected
