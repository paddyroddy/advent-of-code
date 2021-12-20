import numpy as np

CALLED = -1
GRID_LABELS = dict(row=1, col=2)
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


def check_for_row_or_col_match(grids: np.ndarray, table: str) -> bool:
    """
    checks that an entire row or column has been matched
    """
    return grids.sum(axis=GRID_LABELS[table]) == CALLED * GRID_SIZE[f"n_{table}s"]


def compute_bingo_score(matched_grid: np.ndarray, final_number: int) -> int:
    """
    computes the score for the matched bingo grid
    """
    matched_grid[matched_grid == CALLED] = 0
    return matched_grid.sum() * final_number
