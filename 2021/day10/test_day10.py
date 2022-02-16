import numpy as np
import pytest
from day10 import compute_total_syntax_error_score, read_data


@pytest.fixture
def dummy_data() -> np.ndarray:
    return read_data("dummy_day10.txt")


def test_corrupted_char_score(dummy_data) -> None:
    """
    checks if the computed corruption score is correct
    """
    expected = 26397
    computed = compute_total_syntax_error_score(dummy_data)
    assert computed == expected
