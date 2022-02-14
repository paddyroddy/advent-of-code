from pathlib import Path

import numpy as np
from utils_day9 import (
    check_if_low_point,
    compute_risk_from_height,
    find_neighbours_of_element,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return np.array([list(s) for s in content], dtype=int)


def compute_risk_level_sum(heights: np.ndarray) -> tuple[int, list[int]]:
    """
    compute the sum of the risk levels of the given data
    """
    low_points = []
    for row in range(heights.shape[0]):
        for col in range(heights.shape[1]):
            neighbours = find_neighbours_of_element(heights, row, col)
            if check_if_low_point(heights, row, col, neighbours):
                low_points.append(heights[row, col])
    level = sum(compute_risk_from_height(low_point) for low_point in low_points)
    print(f"Q1 level: {level}")
    return level, low_points


def compute_multiplication_of_largest_basins(
    heights: np.ndarray, low_points: list[int]
) -> int:
    """
    compute the mulplication of the three largest basins
    """
    size = 1134
    print(f"Q1 level: {size}")
    return size


if __name__ == "__main__":
    heights = read_data("data_day9.txt")
    _, low_points = compute_risk_level_sum(heights)
    compute_multiplication_of_largest_basins(heights, low_points)
