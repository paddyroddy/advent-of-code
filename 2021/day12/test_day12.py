import numpy as np
import pytest
from day12 import read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day12.csv")
