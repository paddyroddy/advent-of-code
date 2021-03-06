from pathlib import Path

import numpy as np
import pandas as pd
from utils_day7 import (
    compute_fuel_cost_which_increases_with_more_movement,
    move_all_crabs_to_specified_position,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    df = pd.read_csv(_data_path / filename, header=None)
    return df.values[0]


def compute_minimum_fuel_cost(crabs: np.ndarray) -> int:
    """
    find the minimum fuel cost for the given list of crabs
    """
    cost = np.inf
    for position in crabs:
        new_cost = move_all_crabs_to_specified_position(crabs, position)
        cost = new_cost if new_cost < cost else cost
    print(f"Q1 cost: {cost}")
    return cost


def compute_new_minimum_fuel_cost(crabs: np.ndarray) -> int:
    """
    find the minimum fuel cost for the given list of crabs but where
    fuel price increases for more successive moves for an individual crab
    """
    cost = np.inf
    for position in crabs:
        new_cost = compute_fuel_cost_which_increases_with_more_movement(crabs, position)
        cost = new_cost if new_cost < cost else cost
    print(f"Q2 cost: {cost}")
    return cost


if __name__ == "__main__":
    crabs = read_data("data_day7.csv")
    compute_minimum_fuel_cost(crabs)
    compute_new_minimum_fuel_cost(crabs)
