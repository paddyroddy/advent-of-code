import numpy as np
import pytest
from day9 import read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day9.csv")
