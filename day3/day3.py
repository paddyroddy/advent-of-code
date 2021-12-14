from pathlib import Path

import pandas as pd
from utils_day3 import convert_str_to_bool, extract_rate_as_int

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent
name = "binary"


def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(_data_path / filename, names=[name], dtype=str)


def compute_power_consumption_submarine(df: pd.DataFrame) -> int:
    """
    compute the power consumption of the submarines
    """
    # read in data and split into columns of 0 and 1
    df_split = df[name].str.split("", expand=True).iloc[:, 1:-1]

    # most common value
    df_most_common = convert_str_to_bool(df_split.mode())
    df_least_common = ~df_most_common

    # compute product
    gamma_rate = extract_rate_as_int(df_most_common)
    epsilon_rate = extract_rate_as_int(df_least_common)
    product = gamma_rate * epsilon_rate
    print(f"Q1 product: {product}")
    return product


if __name__ == "__main__":
    df = read_data("data_day3.csv")
    compute_power_consumption_submarine(df)
