from day1 import find_largest_measurements, fine_largest_sums


def test_number_depth_increases() -> None:
    """
    checks that the number of times increased matches the expected
    """
    expected = 7
    computed = find_largest_measurements("dummy_day1.csv")
    assert computed == expected


def test_sliding_window() -> None:
    """
    checks that the sum of sliding window increases as expected
    """
    expected = 5
    computed = fine_largest_sums("dummy_day1.csv")
    assert computed == expected
