from pathlib import Path

import pandas as pd
from utils_day5 import (
    NAMES,
    compute_points_which_overlap_twice,
    create_output_grid,
    fill_values_in_grid,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(_data_path / filename, sep=",|->", engine="python", names=NAMES)


def compute_how_many_points_overlap(df: pd.DataFrame) -> int:
    """
    determine the number of points where at least two lines overlap
    """
    grid = create_output_grid(df)
    filled_grid = fill_values_in_grid(grid, df)
    points = compute_points_which_overlap_twice(filled_grid)
    print(f"Q1 points: {points}")
    return points


if __name__ == "__main__":
    df = read_data("data_day5.txt")
    compute_how_many_points_overlap(df)
