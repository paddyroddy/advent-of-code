import pandas as pd
import pytest
from day8 import count_digits_1_4_7_8, count_total_output_value, read_data


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day8.txt")


def test_number_of_1_4_7_8(dummy_data) -> None:
    """
    checks the number of specific digits is as expected
    """
    expected = 26
    computed = count_digits_1_4_7_8(dummy_data)
    assert computed == expected


def test_total_output_values(dummy_data) -> None:
    """
    checks the total numbr of output values map correctly
    """
    expected = 61229
    computed = count_total_output_value(dummy_data)
    assert computed == expected
