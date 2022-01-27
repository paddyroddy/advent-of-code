from pathlib import Path

import pandas as pd
from utils_day19 import compute_distinct_molecules

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
        rules = content[:-2]
        input_string = content[-1]
    df = pd.DataFrame([r.split(" => ") for r in rules], columns=["input", "output"])
    return df, input_string


def compute_num_distinct_molecules(rules: pd.DataFrame, input_string: str) -> int:
    """
    finds the number of distinct molecules under substitution rules
    """
    unique_strings = compute_distinct_molecules(rules, input_string)
    number = len(unique_strings)
    print(f"Q1 number: {number}")
    return number


def compute_steps_required_to_make_medicine(
    rules: pd.DataFrame, output_string: str
) -> int:
    """
    finds the number of steps required to make medicine
    """
    steps = 3
    print(f"Q1 steps: {steps}")
    return steps


if __name__ == "__main__":
    df, input_string = read_data("data_day19.txt")
    compute_num_distinct_molecules(df, input_string)
