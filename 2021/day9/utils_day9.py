import numpy as np


def find_neighbours_of_element(
    data: np.ndarray, row: int, col: int, num_neighbour: int = 1
) -> set[tuple[int, int]]:
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
    return set(neighbours)


def compute_risk_from_height(height: int) -> int:
    """
    compute the risk level of the given height
    """
    return height + 1


def check_if_low_point(
    heights: np.ndarray, row: int, col: int, neighbours: set[tuple[int, int]]
) -> bool:
    """
    check if the given element is a low point
    """
    return all(heights[row, col] <= heights[neighbour] for neighbour in neighbours)


def recursive_check_in_basin(
    data: np.ndarray,
    point: tuple[int, int],
) -> int:
    """
    check if the given element is in the current basin
    """
    size = 0
    if data[point] != -1 and data[point] != 9:
        size = 1
        data[point] = -1
        neighbours = find_neighbours_of_element(data, *point)
        for neighbour in neighbours:
            size += recursive_check_in_basin(data, neighbour)
    return size


def multiply_three_largest(basin_sizes: dict[tuple[int, int], int]) -> int:
    """
    final result is the multiplication of the three largest basins
    """
    return np.prod(sorted(basin_sizes, reverse=True)[:3])
