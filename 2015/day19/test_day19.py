import pandas as pd
import pytest
from day19 import (
    compute_num_distinct_molecules,
    compute_steps_required_to_make_medicine,
    read_data,
)


@pytest.fixture
def dummy_data() -> tuple[pd.DataFrame, str]:
    return read_data("dummy_day19.txt")


def test_num_distinct_molecules(dummy_data) -> None:
    """
    checks the number of distinct molecules as expected
    """
    expected = 4
    computed = compute_num_distinct_molecules(*dummy_data)
    assert computed == expected


@pytest.mark.parametrize("output_string,expected", [("HOH", 3), ("HOHOHOH", 6)])
def test_steps_required_to_make_medicine(dummy_data, output_string, expected) -> None:
    """
    compute the number of steps required to make medicine
    """
    computed = compute_steps_required_to_make_medicine(dummy_data[0], output_string)
    assert computed == expected
