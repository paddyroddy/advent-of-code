import pandas as pd
import pytest
from day8 import read_data


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day8.txt")
