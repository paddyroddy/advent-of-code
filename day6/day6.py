from pathlib import Path

import numpy as np
import pandas as pd
from utils_day6 import BREEDING_TIME, REPRODUCE_TIME, increment_day

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> np.ndarray:
    df = pd.read_csv(_data_path / filename, header=None)
    return df.values[0]


def compute_number_of_lantern_fish(fishes: np.ndarray, days: int) -> int:
    """
    determine the number of lantern fish present after a given number of days
    """
    for _ in range(days):
        fishes = increment_day(fishes)
    number = len(fishes)
    print(f"Q1 number: {number}")
    return number


def simplified_sum_of_lantern_fish(fishes: np.ndarray, days: int) -> int:
    """
    in reality part 1 will take far too long for 256 days
    here the aim is to just keep track of the total number
    and not the list of the individual timers
    """
    # initialise current number of fish
    state = np.zeros(BREEDING_TIME, dtype=int)

    # update the current number of fish per day
    for fish in fishes:
        state[fish] += 1

    # loop through days and update the current state
    for day in range(days):
        today = day % len(state)
        state[(today + REPRODUCE_TIME) % len(state)] += state[today]

    # produce output
    number = state.sum()
    print(f"Q2 number: {number}")
    return number


if __name__ == "__main__":
    fishes = read_data("data_day6.csv")
    compute_number_of_lantern_fish(fishes, 80)
    simplified_sum_of_lantern_fish(fishes, 256)
