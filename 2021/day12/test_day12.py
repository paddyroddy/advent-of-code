import pytest
from day12 import compute_how_many_paths, read_data


@pytest.mark.parametrize("filename,expected", [(1, 10), (2, 19), (3, 226)])
def test_number_of_unique_paths(filename, expected) -> None:
    """
    check the number of unique paths are as expected
    """
    dummy_data = read_data(f"dummy_{filename}_day12.csv")
    computed = compute_how_many_paths(dummy_data)
    assert computed == expected
