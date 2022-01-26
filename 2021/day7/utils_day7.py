import numpy as np


def move_all_crabs_to_specified_position(crabs: np.ndarray, position: int) -> int:
    """
    compute the fuel cost of moving all crabs to specified position
    """
    return np.abs(crabs - position).sum()
