from pathlib import Path

import numpy as np
from utils_day4 import convert_grids_to_array_of_ints, convert_numbers_to_list_of_ints

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[list[int], np.ndarray]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
        numbers = content[0]
        grids = content[2:]
    return convert_numbers_to_list_of_ints(numbers), convert_grids_to_array_of_ints(
        grids
    )


# def find_who_won_bingo_and_compute_score(df: pd.DataFrame) -> int:
#     """
#     what will your final score be if you choose that board
#     """
#     numbers = df.iloc[0]
#     grids = df.iloc[1:]


if __name__ == "__main__":
    numbers, grids = read_data("dummy_day4.txt")
    print()
