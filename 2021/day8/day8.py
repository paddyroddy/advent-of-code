import re
from pathlib import Path

import pandas as pd
from utils_day8 import (
    SEGMENTS,
    UNIQUE_NUMBERS,
    compute_final_count,
    create_columns,
    find_all_string_lengths,
    map_the_length_5_digits,
    map_the_length_6_digits,
    map_the_unique_letters,
)

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    df = pd.DataFrame(
        [re.split(r"\s\|\s|\s", c) for c in content], columns=create_columns(content)
    )
    return df.applymap(lambda x: "".join(sorted(x)))


def count_digits_1_4_7_8(notes: pd.DataFrame) -> int:
    """
    count the number of digits in the output that are 1, 4, 7, or 8
    which have a unique number of segments and hence are easy to calculate
    """
    df_output = notes.iloc[:, notes.columns.str.startswith("output")]
    string_lengths = find_all_string_lengths(df_output)
    count = string_lengths.isin([SEGMENTS[u] for u in UNIQUE_NUMBERS]).values.sum()
    print(f"Q1 count: {count}")
    return count


def count_total_output_value(notes: pd.DataFrame) -> int:
    """
    count the total value of each output set of numbers
    """
    # working with pandas directly became unmanageable
    # split into input and output columns
    input_array = notes.iloc[:, notes.columns.str.startswith("input")].values
    output_array = notes.iloc[:, notes.columns.str.startswith("output")].values

    # initialise count
    count = 0

    for i in range(len(input_array)):
        # create a unique letter mapping dict per loop
        letter_mappings: dict[int, str] = dict()

        map_the_unique_letters(input_array[i], letter_mappings)
        map_the_length_6_digits(input_array[i], letter_mappings)
        map_the_length_5_digits(input_array[i], letter_mappings)
        count += compute_final_count(output_array[i], letter_mappings)

    print(f"Q2 count: {count}")
    return count


if __name__ == "__main__":
    notes = read_data("data_day8.txt")
    count_digits_1_4_7_8(notes)
    count_total_output_value(notes)
