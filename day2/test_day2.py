import pandas as pd
import pytest

from day2 import (
    compute_horizontal_depth_product,
    compute_product_factoring_in_aim,
    read_data,
)


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day2.csv")


def test_product_as_expected(dummy_data) -> None:
    """
    checks the horizontal depth product is as expected
    """
    expected = 150
    computed = compute_horizontal_depth_product(dummy_data)
    assert computed == expected


def test_product_aim_as_expected(dummy_data) -> None:
    """
    checks the product with aim is as expected
    """
    expected = 900
    computed = compute_product_factoring_in_aim(dummy_data)
    assert computed == expected
