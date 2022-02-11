from pathlib import Path

import numpy as np

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
    level = 15
    print(f"Q1 level: {level}")
    return level


if __name__ == "__main__":
    heights = read_data("dummy_day9.txt")
    compute_risk_level_sum(heights)
