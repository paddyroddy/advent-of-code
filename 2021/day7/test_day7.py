import numpy as np
import pytest
from day7 import compute_minimum_fuel_cost, read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day7.csv")


def test_fuel_cost(dummy_data) -> None:
    """
    checks the amount of fuel is as expected
    """
    expected = 37
    computed = compute_minimum_fuel_cost(dummy_data)
    assert computed == expected
