import pandas as pd
import pytest

from day4 import read_data


@pytest.fixture
def dummy_data() -> pd.DataFrame:
    return read_data("dummy_day4.csv")


# def test_bingo_score_as_expected(dummy_data) -> None:
#     """
#     checks the bingo score is as expected
#     """
#     expected = 4512
#     computed = find_who_won_bingo_and_compute_score(dummy_data)
#     assert computed == expected
