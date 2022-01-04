import numpy as np
import pandas as pd

NAMES = ["x1", "y1", "x2", "y2"]


def _swap_index_order_for_slcing(idx1: int, idx2: int) -> tuple[int, int]:
    """
    for slicing require smaller index to be first
    """
    idx1, idx2 = (idx1, idx2) if idx1 < idx2 else (idx2, idx1)
    return idx1, idx2 + 1


def _fill_horizontal_lines(grid: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    helper function to fill the horizontal lines in the grid
    """
    horizontal = df[NAMES[1]] == df[NAMES[3]]
    for _, row in df.loc[horizontal].iterrows():
        x1, x2 = _swap_index_order_for_slcing(row[NAMES[0]], row[NAMES[2]])
        grid[row[NAMES[1]], x1:x2] += 1
    return grid


def _fill_vertical_lines(grid: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    helper function to fill the vertical lines in the grid
    """
    vertical = df[NAMES[0]] == df[NAMES[2]]
    for _, row in df.loc[vertical].iterrows():
        y1, y2 = _swap_index_order_for_slcing(row[NAMES[1]], row[NAMES[3]])
        grid[y1:y2, row[NAMES[0]]] += 1
    return grid


def create_output_grid(df: pd.DataFrame) -> np.ndarray:
    """
    create a grid of zeros with the same size as the input dataframe
    """
    size = df.max().max() + 1
    return np.zeros((size, size))


def fill_values_in_grid(grid: np.ndarray, df: pd.DataFrame) -> np.ndarray:
    """
    fill the grid with the values of the input dataframe
    """
    grid = _fill_horizontal_lines(grid, df)
    grid = _fill_vertical_lines(grid, df)
    return grid


def compute_points_which_overlap_twice(grid: np.ndarray) -> int:
    """
    compute the number of points where at least two lines overlap
    """
    return (grid > 1).sum()
