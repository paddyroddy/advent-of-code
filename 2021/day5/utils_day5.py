import numpy as np
import pandas as pd


def _swap_index_order_for_slcing(idx1: int, idx2: int) -> tuple[int, int]:
    """
    for slicing require smaller index to be first
    """
    idx1, idx2 = (idx1, idx2) if idx1 < idx2 else (idx2, idx1)
    return idx1, idx2 + 1


def _compute_horizontal_lines(df) -> pd.DataFrame:
    """
    create mask for horizontal lines
    """
    return df["y1"] == df["y2"]


def _compute_vertical_lines(df) -> pd.DataFrame:
    """
    create mask for vertical lines
    """
    return df["x1"] == df["x2"]


def _find_sign(coord1: int, coord2: int) -> int:
    """
    helper method to check if numbers decreasing in order
    """
    return np.sign(coord2 - coord1)


def create_output_grid(df: pd.DataFrame) -> np.ndarray:
    """
    create a grid of zeros with the same size as the input dataframe
    """
    size = df.max().max() + 1
    return np.zeros((size, size))


def fill_horizontal_lines(grid: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    helper function to fill the horizontal lines in the grid
    """
    horizontal = _compute_horizontal_lines(df)
    for _, row in df.loc[horizontal].iterrows():
        x1, x2 = _swap_index_order_for_slcing(row["x1"], row["x2"])
        grid[x1:x2, row["y1"]] += 1
    return grid


def fill_vertical_lines(grid: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    helper function to fill the vertical lines in the grid
    """
    vertical = _compute_vertical_lines(df)
    for _, row in df.loc[vertical].iterrows():
        y1, y2 = _swap_index_order_for_slcing(row["y1"], row["y2"])
        grid[row["x1"], y1:y2] += 1
    return grid


def fill_diagonal_lines(grid: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    helper function to fill the diagonal lines in the grid
    """
    horizontal = _compute_horizontal_lines(df)
    vertical = _compute_vertical_lines(df)
    diagonal = ~horizontal & ~vertical
    for _, row in df.loc[diagonal].iterrows():
        x_sign = _find_sign(row["x1"], row["x2"])
        y_sign = _find_sign(row["y1"], row["y2"])
        for x, y in zip(
            range(row["x1"], row["x2"] + x_sign, x_sign),
            range(row["y1"], row["y2"] + y_sign, y_sign),
        ):
            grid[x, y] += 1
    return grid


def compute_points_which_overlap_twice(grid: np.ndarray) -> int:
    """
    compute the number of points where at least two lines overlap
    """
    return (grid > 1).sum()
