from pathlib import Path

import pandas as pd

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(_data_path / filename, header=None)


def find_largest_measurements(df: pd.DataFrame) -> int:
    """
    how many measurements are larger than the previous measurement
    """
    number_increased = int((df.diff() > 0).sum())
    print(f"Q1 number increased: {number_increased}")
    return number_increased


def fine_largest_sums(df: pd.DataFrame) -> int:
    """
    how many sums are larger than the previous sum
    """
    window = 3
    window_increased = int((df.rolling(window=window).sum().diff() > 0).sum())
    print(f"Q2 window increased: {window_increased}")
    return window_increased


if __name__ == "__main__":
    df = read_data("data_day1.csv")
    find_largest_measurements(df)
    fine_largest_sums(df)
