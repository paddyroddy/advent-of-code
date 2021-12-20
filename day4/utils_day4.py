import numpy as np

CALLED = -1
GRID_SIZE = dict(n_rows=5, n_cols=5)


def convert_numbers_to_list_of_ints(numbers: str) -> list[int]:
    """
    the called numbers are read in as a string originally
    """
    return list(map(int, numbers.split(",")))


def convert_grids_to_array_of_ints(grids: list[str]) -> np.ndarray:
    """
    the bingo grids are read in as a string originally
    """
    cleaned_array = np.array([x.split() for x in filter(None, grids)], dtype=int)
    return cleaned_array.reshape(-1, GRID_SIZE["n_rows"], GRID_SIZE["n_cols"])
