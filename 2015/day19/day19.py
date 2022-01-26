from pathlib import Path

import pandas as pd

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
        rules = content[:-2]
        string = content[-1]
    df = pd.DataFrame([r.split(" => ") for r in rules], columns=["input", "output"])
    return df, string


def compute_num_distinct_molecules(rules: pd.DataFrame, string: str) -> int:
    """
    finds the number of distinct molecules under substitution rules
    """
    for _, rule in rules.iterrows():
        new_string = string.replace(rule["input"], rule["output"], 1)
    print(f"Q1 number: {number}")
    return number


if __name__ == "__main__":
    df, string = read_data("dummy_day19.txt")
    compute_num_distinct_molecules(df, string)
