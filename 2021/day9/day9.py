from pathlib import Path

import numpy as np
from utils_day9 import (
    check_if_low_point,
    compute_risk_from_height,
    find_neighbours_of_element,
    multiply_largest,
    recursive_check_in_basin,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return np.array([list(s) for s in content], dtype=int)


def compute_risk_level_sum(heights: np.ndarray) -> tuple[int, list[tuple[int, int]]]:
    """
    compute the sum of the risk levels of the given data
    """
    low_points: list[tuple[int, int]] = list()
    for row in range(heights.shape[0]):
        for col in range(heights.shape[1]):
            neighbours = find_neighbours_of_element(heights, row, col)
            if check_if_low_point(heights, row, col, neighbours):
                low_points.append((row, col))
    level = sum(
        compute_risk_from_height(heights[low_point]) for low_point in low_points
    )
    print(f"Q1 level: {level}")
    return level, low_points


def compute_multiplication_of_largest_basins(
    heights: np.ndarray, low_points: list[tuple[int, int]]
) -> int:
    """
    compute the mulplication of the three largest basins
    """
    basin_size: dict[tuple[int, int], int] = dict()
    for low_point in low_points:
        basin_size[low_point] = recursive_check_in_basin(heights, low_point)
    size = multiply_largest(basin_size, 3)
    print(f"Q2 size: {size}")
    return size


if __name__ == "__main__":
    heights = read_data("data_day9.txt")
    _, low_points = compute_risk_level_sum(heights)
    compute_multiplication_of_largest_basins(heights, low_points)
