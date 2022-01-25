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
    product = int(horizontal * depth)
    print(f"Q1 product: {product}")
    return product


def compute_product_factoring_in_aim(df: pd.DataFrame) -> int:
    """
    tracking aim in addition to depth and direction
    """
    # initialise columns
    df["cumulative_depth"] = 0
    df["cumulative_horizontal"] = 0
    df["horizontal"] = 0
    df["depth"] = 0
    df["aim"] = 0

    # create boolean masks
    forward_direction = df["direction"] == "forward"
    up_direction = df["direction"] == "up"

    # set up direction to negative depth and relabel to down
    df.loc[up_direction, "amount"] *= -1
    df.loc[up_direction, "direction"] = "down"

    # fill in horizontal values
    df.loc[forward_direction, "horizontal"] = df.loc[forward_direction, "amount"]
    df.loc[forward_direction, "cumulative_horizontal"] = df["horizontal"].cumsum()

    # fill in aim values
    df.loc[forward_direction, "amount"] = 0
    df["aim"] = df["amount"].cumsum()

    # fill in depth values
    df.loc[forward_direction, "depth"] += (
        df.loc[forward_direction, "aim"] * df.loc[forward_direction, "horizontal"]
    )
    df["cumulative_depth"] = df["depth"].cumsum()

    # compute product
    final_row = df.iloc[-1]
    product = int(final_row["cumulative_horizontal"] * final_row["cumulative_depth"])
    print(f"Q2 product: {product}")
    return product


if __name__ == "__main__":
    df = read_data("data_day2.csv")
    compute_horizontal_depth_product(df)
    compute_product_factoring_in_aim(df)
