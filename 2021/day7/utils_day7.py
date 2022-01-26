import numpy as np


def _triangular_number(n: int) -> int:
    """
    compute the nth triangular number
    """
    return n * (n + 1) // 2


def move_all_crabs_to_specified_position(crabs: np.ndarray, position: int) -> int:
    """
    compute the fuel cost of moving all crabs to specified position
    """
    return np.abs(crabs - position).sum()


def compute_fuel_cost_which_increases_with_more_movement(
    crabs: np.ndarray, position: int
) -> int:
    """
    compute fuel cost per crab but where the first step costs 1,
    the second step costs 2, the third step costs 3, and so on
    """
    fuel = 0
    for crab in crabs:
        fuel += _triangular_number(abs(crab - position))
    return fuel
