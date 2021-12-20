from pathlib import Path

import numpy as np
from utils_day4 import (
    CALLED,
    check_for_row_or_col_match,
    compute_bingo_score,
    convert_grids_to_array_of_ints,
    convert_numbers_to_list_of_ints,
)

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


def find_who_won_bingo_and_compute_score(numbers: list[int], grids: np.ndarray) -> int:
    """
    what will your final score be if you choose that board
    """
    for num in numbers:
        grids[grids == num] = CALLED
        match = np.where(
            check_for_row_or_col_match(grids, "row")
            | check_for_row_or_col_match(grids, "col")
        )[0]
        if match.size > 0:
            # if match found then exit the loop
            bingo_grid = grids[match]
            break
    score = compute_bingo_score(bingo_grid, num)
    print(f"Q1 score: {score}")
    return score


if __name__ == "__main__":
    numbers, grids = read_data("data_day4.txt")
    find_who_won_bingo_and_compute_score(numbers, grids)
