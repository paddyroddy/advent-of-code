import numpy as np
import pytest
from day19 import compute_num_distinct_molecules, read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day19.txt")


def test_num_distinct_molecules(dummy_data) -> None:
    """
    checks the number of distinct molecules as expected
    """
    expected = 4
    computed = compute_num_distinct_molecules(dummy_data)
    assert computed == expected
