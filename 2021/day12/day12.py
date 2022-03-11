from pathlib import Path

import pandas as pd
from utils_day12 import convert_df_to_dict, recursive_check_for_paths

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> dict[str, list[str]]:
    df = pd.read_csv(_data_path / filename, sep="-", header=None)
    return convert_df_to_dict(df)


def compute_how_many_paths(data: dict[str, list[str]]) -> int:
    """
    given that you can pass through large paths multiple times but
    small caves only once, what are the total number of paths that
    travel from the start to the end?
    """
    paths = len(recursive_check_for_paths(data, "start", "end", [], []))
    print(f"Q1 paths: {paths}")
    return paths


if __name__ == "__main__":
    connections = read_data("data_day12.csv")
    compute_how_many_paths(connections)
