import numpy as np
import pandas as pd

SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
UNIQUE_NUMBERS = [1, 4, 7, 8]


def create_columns(content: list[str]) -> list[str]:
    """
    create columns for the initial dataframe the format is of
    <a> ... <b> | <c> ... <d>
    """
    first_line = content[0]
    split_at_pipe = first_line.split("|")
    n_input = split_at_pipe[0].count(" ")
    n_output = split_at_pipe[1].count(" ")
    input_columns = [f"input{i}" for i in range(n_input)]
    output_columns = [f"output{o}" for o in range(n_output)]
    return input_columns + output_columns


def find_all_string_lengths(df: pd.DataFrame) -> pd.DataFrame:
    """
    helper method to find length of all strings in a dataframe
    """
    return df.applymap(lambda x: len(x))


def map_the_unique_letters(
    input_array: np.ndarray, letter_mappings: dict[int, str]
) -> None:
    """
    for these digits the number of segments is unique
    """
    for digits in input_array:
        for u in UNIQUE_NUMBERS:
            if len(digits) == SEGMENTS[u]:
                letter_mappings[u] = digits
                break


def map_the_length_6_digits(
    input_array: np.ndarray, letter_mappings: dict[int, str]
) -> None:
    """
    map the special case of 6 digits which holds for 3
    """
    for digits in input_array:
        if len(digits) == 6:
            # 4 is wholly contained within 9
            if set(letter_mappings[4]).issubset(set(digits)):
                letter_mappings[9] = digits

            # 1 is wholly contained within 0
            elif set(letter_mappings[1]).issubset(set(digits)):
                letter_mappings[0] = digits

            else:
                letter_mappings[6] = digits


def map_the_length_5_digits(
    input_array: np.ndarray, letter_mappings: dict[int, str]
) -> None:
    """
    map the special case of 5 digits which holds for 3
    """
    for digits in input_array:
        if len(digits) == 5:
            # 5 is wholly contained within 6
            if set(digits).issubset(set(letter_mappings[6])):
                letter_mappings[5] = digits

            # 1 is wholly contained within 3
            elif set(letter_mappings[1]).issubset(set(digits)):
                letter_mappings[3] = digits

            else:
                letter_mappings[2] = digits


def compute_final_count(
    output_array: np.ndarray, letter_mappings: dict[int, str]
) -> int:
    """
    create count of the final output per row
    """
    number = []
    for digits in output_array:
        for key, value in letter_mappings.items():
            if set(digits) == set(value):
                number.append(str(key))
    return int("".join(number))
