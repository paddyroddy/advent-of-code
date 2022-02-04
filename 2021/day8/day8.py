import re
from pathlib import Path

import pandas as pd
from utils_day8 import (  # determine_character_mappings,
    DISPLAY,
    create_columns,
    find_all_string_lengths,
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
    output_df = notes.iloc[:, notes.columns.str.startswith("output")]
    string_lengths = find_all_string_lengths(output_df)
    numbers_of_interest = {1, 4, 7, 8}
    count = string_lengths.isin(
        DISPLAY.loc[numbers_of_interest].sum(axis="columns").values
    ).values.sum()
    print(f"Q1 count: {count}")
    return count


def count_total_output_value(notes: pd.DataFrame) -> int:
    """
    count the total value of each output set of numbers
    """
    # string_lengths = find_all_string_lengths(notes)
    # letter_mappings = determine_character_mappings(notes, string_lengths)
    # one = find_letters_representing_string_length(notes, string_lengths, 1)
    # seven = find_letters_representing_string_length(notes, string_lengths, 7)
    # LETTER_MAPPING["a"] = remove_characters_from_df(seven, one)
    # eight = find_letters_representing_string_length(notes, string_lengths, 8)
    # zero = find_letters_representing_string_length(notes, string_lengths, 0)
    # LETTER_MAPPING["d"] = remove_characters_from_df(eight, zero)
    # six = find_letters_representing_string_length(notes, string_lengths, 6)
    # five = find_letters_representing_string_length(notes, string_lengths, 5)
    # LETTER_MAPPING["e"] = remove_characters_from_df(six, five)
    # nine = find_letters_representing_string_length(notes, string_lengths, 9)
    return 0


if __name__ == "__main__":
    notes = read_data("dummy_day8.txt")
    # count_digits_1_4_7_8(notes)
    count_total_output_value(notes)
