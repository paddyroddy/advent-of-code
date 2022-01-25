import pandas as pd
import pytest
from day3 import (
    compute_life_support_rating_submarine,
    compute_power_consumption_submarine,
    read_data,
)


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day3.csv")


def test_power_consumption_as_expected(dummy_data) -> None:
    """
    checks the gamma and epsilon product as expected
    """
    expected = 198
    computed = compute_power_consumption_submarine(dummy_data)
    assert computed == expected


def test_life_support_as_expected(dummy_data) -> None:
    """
    checks the oxygen generator and CO2 scrubber product as expected
    """
    expected = 230
    computed = compute_life_support_rating_submarine(dummy_data)
    assert computed == expected
