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


def compute_risk_level_sum(heights: np.ndarray) -> int:
    """
    compute the sum of the risk levels of the given data
    """
    low_points = []
    for row in range(heights.shape[0]):
        for col in range(heights.shape[1]):
            neighbours = find_neighbours_of_element(heights, row, col)
            if check_if_low_point(heights, row, col, neighbours):
                low_points.append(compute_risk_from_height(heights, row, col))
    level = sum(low_points)
    print(f"Q1 level: {level}")
    return level


if __name__ == "__main__":
    heights = read_data("data_day9.txt")
    compute_risk_level_sum(heights)
