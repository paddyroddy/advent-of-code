import numpy as np


def find_neighbours_of_element(
    data: np.ndarray, row: int, col: int, num_neighbour: int = 1
) -> list[int]:
    """
    find the horizontal and vertical neighbours of the element at the given index
    """
    neighbours = []
    for r in range(-num_neighbour, num_neighbour + 1):
        curr_row = row + r
        if curr_row >= 0 and curr_row <= data.shape[0] - 1:
            for colAdd in range(-num_neighbour, num_neighbour + 1):
                curr_col = col + colAdd
                if curr_col >= 0 and curr_col <= data.shape[1] - 1:
                    if curr_col == col and curr_row == row:
                        continue
                    neighbours.append(data[curr_row][curr_col])
    return neighbours


def compute_risk_from_height(heights: np.ndarray, row: int, col: int) -> int:
    """
    compute the risk level of the given height
    """
    return heights[row, col] + 1


def check_if_low_point(
    heights: np.ndarray, row: int, col: int, neighbours: list[int]
) -> bool:
    """
    check if the given element is a low point
    """
    return all(heights[row, col] <= neighbours)
