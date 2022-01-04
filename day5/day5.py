from pathlib import Path

import pandas as pd
from utils_day5 import (
    compute_points_which_overlap_twice,
    create_output_grid,
    fill_diagonal_lines,
    fill_horizontal_lines,
    fill_vertical_lines,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(
        _data_path / filename,
        sep=",|->",
        engine="python",
        names=["x1", "y1", "x2", "y2"],
    )


def compute_how_many_points_overlap(df: pd.DataFrame) -> int:
    """
    determine the number of points where at least two lines overlap
    """
    grid = create_output_grid(df)
    grid = fill_horizontal_lines(grid, df)
    grid = fill_vertical_lines(grid, df)
    points = compute_points_which_overlap_twice(grid)
    print(f"Q1 points: {points}")
    return points


def compute_overlapping_points_with_diagonals(df: pd.DataFrame) -> int:
    """
    determine the number of points where at least two lines overlap
    factoring in diagonal lines as well as horizontal and vertical
    """
    grid = create_output_grid(df)
    grid = fill_horizontal_lines(grid, df)
    grid = fill_vertical_lines(grid, df)
    grid = fill_diagonal_lines(grid, df)
    points = compute_points_which_overlap_twice(grid)
    print(f"Q2 points: {points}")
    return points


if __name__ == "__main__":
    df = read_data("data_day5.txt")
    compute_how_many_points_overlap(df)
    compute_overlapping_points_with_diagonals(df)
