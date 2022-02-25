import pytest
from day11 import read_data


@pytest.fixture
def dummy_data() -> list[str]:
    return read_data("dummy_day11.txt")
