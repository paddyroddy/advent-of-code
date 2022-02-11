from pathlib import Path

import numpy as np
import pandas as pd

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    df = pd.read_csv(_data_path / filename, header=None)
    return df.values[0]


if __name__ == "__main__":
    data = read_data("dummy_day9.csv")
