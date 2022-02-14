import numpy as np


def find_neighbours_of_element(
    data: np.ndarray, row: int, col: int, num_neighbour: int = 1
) -> list[tuple[int, int]]:
    """
    find the horizontal and vertical neighbours of the element at the given index
    """
    neighbours: list[tuple[int, int]] = []
    for r in range(-num_neighbour, num_neighbour + 1):
        curr_row = row + r
        if curr_row >= 0 and curr_row <= data.shape[0] - 1:
            for colAdd in range(-num_neighbour, num_neighbour + 1):
                curr_col = col + colAdd
                if curr_col >= 0 and curr_col <= data.shape[1] - 1:
                    if curr_col == col and curr_row == row:
                        continue
                    neighbours.append((curr_row, curr_col))
    return neighbours


def compute_risk_from_height(height: int) -> int:
    """
    compute the risk level of the given height
    """
    return height + 1


def check_if_low_point(
    heights: np.ndarray, row: int, col: int, neighbours: list[tuple[int, int]]
) -> bool:
    """
    check if the given element is a low point
    """
    return all(heights[row, col] <= heights[neighbour] for neighbour in neighbours)


def recursive_check_in_basin(
    data: np.ndarray, low_point: list[tuple[int, int]]
) -> None:
    """
    check if the given element is in the current basin
    """
    for point in low_point:
        set_of_points = find_neighbours_of_element(data, *point)
        non_nine = [p for p in set_of_points if data[p] != 9]
    return recursive_check_in_basin(data, set_of_points)
