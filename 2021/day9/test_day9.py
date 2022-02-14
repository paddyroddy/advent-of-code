import numpy as np
import pytest
from day9 import (
    compute_multiplication_of_largest_basins,
    compute_risk_level_sum,
    read_data,
)


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day9.txt")


@pytest.fixture
def risk_level(dummy_data) -> tuple[int, list[int]]:
    return compute_risk_level_sum(dummy_data)


def test_risk_level_as_expected(risk_level) -> None:
    """
    check risk level sum is anticiapted
    """
    expected = 15
    assert risk_level[0] == expected


def test_basin_size_as_expected(risk_level) -> None:
    """
    check risk level sum is anticiapted
    """
    expected = 1134
    computed = compute_multiplication_of_largest_basins(dummy_data, risk_level[1])
    assert computed == expected
