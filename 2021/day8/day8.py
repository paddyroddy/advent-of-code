import re
from pathlib import Path

import pandas as pd
from utils_day8 import SEGMENTS, create_columns

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return pd.DataFrame(
        [re.split(r"\s\|\s|\s", c) for c in content], columns=create_columns(content)
    )


def count_digits_1_4_7_8(notes: pd.DataFrame) -> int:
    """
    count the number of digits in the output that are 1, 4, 7, or 8
    which have a unique number of segments and hence are easy to calculate
    """
    output_df = notes.iloc[:, notes.columns.str.startswith("output")]
    string_lengths = output_df.applymap(lambda x: len(x))
    count = string_lengths.isin(
        [SEGMENTS[1], SEGMENTS[4], SEGMENTS[7], SEGMENTS[8]]
    ).values.sum()
    print(f"Q1 count: {count}")
    return count


if __name__ == "__main__":
    notes = read_data("data_day8.txt")
    count_digits_1_4_7_8(notes)
