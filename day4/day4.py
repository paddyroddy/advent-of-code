from pathlib import Path

import numpy as np
from utils_day4 import (
    CALLED,
    check_for_row_or_col_match,
    check_whole_grids_not_been_called,
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


def find_who_first_won_bingo_and_compute_score(
    numbers: list[int], grids: np.ndarray
) -> int:
    """
    what will your final score be if you choose that board
    """
    for num in numbers:
        # set all matches to some value
        grids[grids == num] = CALLED

        # check for match in any row or column
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


def find_who_last_won_bingo_and_compute_score(
    numbers: list[int], grids: np.ndarray
) -> int:
    """
    once it wins, what would its final score be
    """
    # initialise a bingo matcher tracker
    num_bingo_called = 0
    num_grids = grids.shape[0]

    for num in numbers:
        # set all matches to some value
        grids[grids == num] = CALLED

        # check for match in any row or column in unmatched grids
        # numpy where returns duplicate indices and hence unique is used
        match = np.unique(
            np.where(
                (
                    check_for_row_or_col_match(grids, "row")
                    | check_for_row_or_col_match(grids, "col")
                )
                & check_whole_grids_not_been_called(grids)[:, np.newaxis]
            )[0]
        )

        # check for match
        if len(match) > 0:
            # increment tracker
            num_bingo_called += len(match)

            if num_bingo_called == num_grids:
                # if all grids have been matched then exit the loop
                bingo_grid = grids[match]
                break
            else:
                # set all of matched grid to called
                grids[match] = CALLED

    score = compute_bingo_score(bingo_grid, num)
    print(f"Q2 score: {score}")
    return score


if __name__ == "__main__":
    numbers, grids = read_data("data_day4.txt")
    find_who_first_won_bingo_and_compute_score(numbers, grids)
    find_who_last_won_bingo_and_compute_score(numbers, grids)
