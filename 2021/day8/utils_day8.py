import re

import numpy as np
import pandas as pd

DISPLAY = pd.DataFrame(
    data=[
        [True, True, True, False, True, True, True],
        [False, False, True, False, False, True, False],
        [True, False, True, True, True, False, True],
        [True, False, True, True, False, True, True],
        [False, True, True, True, False, True, False],
        [True, True, False, True, False, True, True],
        [True, True, False, True, True, True, True],
        [True, False, True, False, False, True, False],
        [True, True, True, True, True, True, True],
        [True, True, True, True, False, True, True],
    ],
    columns=["a", "b", "c", "d", "e", "f", "g"],
)


def _find_letters_representing_string_length(
    df_notes: pd.DataFrame, df_str_len: pd.DataFrame, str_len: int
) -> pd.DataFrame:
    """
    helper method to find the letters that represent the string length
    https://stackoverflow.com/a/31861396/7359333
    """
    return (
        df_notes.where(df_str_len == DISPLAY.iloc[str_len].sum())
        .stack()
        .groupby(level=0)
        .first()
        .reindex(df_notes.index)
    )


def _remove_characters_from_df(
    first_instance: dict[int, pd.DataFrame], more_segments: int, fewer_segments: int
) -> pd.DataFrame:
    """
    removes the characters in df_more_char from df_less_char
    """
    # regex used because characters in different orders
    return first_instance[more_segments].combine(
        first_instance[fewer_segments], lambda x, y: re.sub(rf"[{y}]", "", x)
    )


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


def determine_character_mappings(
    df_notes: pd.DataFrame, df_str_len: pd.DataFrame
) -> None:
    """
    determine how each character is mapped in the display
    """
    # create dataframe to store final mappings
    letter_mapping = pd.DataFrame(
        np.empty(DISPLAY.shape, dtype=object), columns=DISPLAY.columns
    )

    # find first instance of each string length
    first_instance = dict()
    for i in range(letter_mapping.shape[0]):
        first_instance[i] = _find_letters_representing_string_length(
            df_notes, df_str_len, i
        )

    # fill in character mapping following rules
    mapping_dict = dict(a=(7, 1), d=(8, 0), e=(6, 5))
    for char, (more_segments, fewer_segments) in mapping_dict.items():
        letter_mapping[char] = _remove_characters_from_df(
            first_instance, more_segments, fewer_segments
        )

    return letter_mapping
