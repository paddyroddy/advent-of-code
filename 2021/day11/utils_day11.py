import numpy as np
import pandas as pd

FLASH = 9
INCREMENT = 1
NAME = "levels"
RESET = 0


def _find_all_neighbours_of_element(
    data: np.ndarray, row: int, col: int
) -> set[tuple[int, int]]:
    """
    find all neighbours of the element at the given index
    """
    # initialise neighbours list
    neighbours: list[tuple[int, int]] = list()

    # find all neighbours
    for r in range(-1, 2):
        for c in range(-1, 2):
            neighbours.append((row + r, col + c))

    # check within bounds
    return set(
        filter(
            lambda coord: 0 <= coord[0] < data.shape[0]
            and 0 <= coord[1] < data.shape[1],
            neighbours,
        )
    )


def _helper_flashing_function(
    energies: np.ndarray, has_flashed: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    helper function to count flashes as the process is recursive
    """
    # check for indices of where output has reached
    # threshold and not previously flashed
    indices = np.where((energies > FLASH) & ~has_flashed)

    # if no indices found then exit
    if not indices[0].size:
        return energies, has_flashed

    # record the flashes octopuses
    has_flashed[indices] = True

    # check if any octopuses have flashed
    for row, col in zip(*indices):
        neighbours = _find_all_neighbours_of_element(energies, row, col)
        for neighbour in neighbours:
            energies[neighbour] += INCREMENT

    # recurse until all increments are complete
    return _helper_flashing_function(energies, has_flashed)


def convert_to_df_of_int(df: pd.DataFrame, name: str) -> np.ndarray:
    """
    take the string dataframe and split it into a dataframe of ints
    """
    return df[name].str.split("", expand=True).iloc[:, 1:-1].astype(int).values


def increment_octopuses_level_and_count_flashes(
    energies: np.ndarray,
) -> tuple[np.ndarray, int]:
    """
    increment the levels of octopuses by 1 and check indices of flashes
    """
    # initialise tracking of whether octopuses have flashed
    has_flashed = np.zeros(energies.shape, dtype=bool)

    # increment all levels by 1
    energies += INCREMENT

    energies, has_flashed = _helper_flashing_function(energies, has_flashed)

    # reset the flashed octopuses
    energies[has_flashed] = RESET

    # compute count
    count = has_flashed.sum()

    return energies, count
