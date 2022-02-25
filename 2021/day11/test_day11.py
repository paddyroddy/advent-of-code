import numpy as np
import pytest
from day11 import count_how_many_flashes, read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day11.csv")


@pytest.mark.parametrize("steps,expected", [(10, 204), (100, 1656)])
def test_num_flashes_as_expected(dummy_data, steps, expected) -> None:
    """
    after a number of steps check the number of flashes are as expected
    """
    computed = count_how_many_flashes(dummy_data, steps)
    assert computed == expected
