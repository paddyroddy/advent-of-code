from puzzle1_day1 import find_largest_measurements


def test_number_depth_increases() -> None:
    """
    checks that the number of times increased matches the expected
    """
    expected = 7
    computed = find_largest_measurements("dummy_day1.csv")
    assert computed == expected
