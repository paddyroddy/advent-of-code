from pathlib import Path

import pandas as pd

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(
        _data_path / filename, names=["direction", "amount"], delim_whitespace=True
    )


def compute_horizontal_depth_product(df: pd.DataFrame) -> int:
    """
    what do you get if you multiply your final horizontal position by your final depth
    """
    grouped = df.groupby(["direction"]).sum()
    horizontal = grouped.loc["forward"]
    depth = grouped.loc["down"] - grouped.loc["up"]
    product = (horizontal * depth)["amount"]
    print(f"Q1 product: {product}")
    return product


if __name__ == "__main__":
    df = read_data("data_day2.csv")
    compute_horizontal_depth_product(df)
    # fine_largest_sums(df)
