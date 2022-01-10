from pathlib import Path

import numpy as np
import pandas as pd
from utils_day6 import compute_number_of_fish, increment_day

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    df = pd.read_csv(_data_path / filename, header=None)
    return df.values[0]


def compute_number_of_lantern_fish(fishes: np.ndarray, days: int) -> int:
    """
    determine the number of points where at least two lines overlap
    """
    for _ in range(days):
        fishes = increment_day(fishes)
    number = compute_number_of_fish(fishes)
    print(f"Q1 number: {number}")
    return number


if __name__ == "__main__":
    fishes = read_data("data_day6.csv")
    compute_number_of_lantern_fish(fishes, 80)
    # compute_overlapping_points_with_diagonals(df)
