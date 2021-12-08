from pathlib import Path

import pandas as pd

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def find_largest_measurements(filename: str) -> int:
    """
    how many measurements are larger than the previous measurement
    """
    df = pd.read_csv(_data_path / filename, header=None)
    number_increased = int((df.diff() > 0).sum())
    print(f"number increased: {number_increased}")
    return number_increased


if __name__ == "__main__":
    find_largest_measurements("data_day1.csv")
