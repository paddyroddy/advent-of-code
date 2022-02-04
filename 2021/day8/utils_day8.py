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
    df_notes: pd.DataFrame, df_str_len: pd.DataFrame, character: int
) -> pd.DataFrame:
    """
    helper method to find the letters that represent the string length
    https://stackoverflow.com/a/31861396/7359333
    """
    return (
        df_notes.where(df_str_len == DISPLAY.loc[character].sum())
        .stack()
        .groupby(level=0)
        .first()
        .reindex(df_notes.index)
    )


# def _remove_characters_from_df(
#     first_instance: dict[int, pd.DataFrame], more_segments: int, fewer_segments: int
# ) -> pd.DataFrame:
#     """
#     removes the characters in df_more_char from df_less_char
#     """
#     # regex used because characters in different orders
#     swap_chars = first_instance[more_segments].combine(
#         first_instance[fewer_segments], lambda x, y: re.sub(rf"[{y}]", "", x)
#     )
#     # if more than one letter returned don't swap
#     swap_chars[swap_chars.str.len() > 1] = None
#     return swap_chars


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
) -> pd.DataFrame:
    """
    determine how each character is mapped in the display
    """
    # avoid overwriting the original dataframe
    letter_mappings = df_notes.copy()

    unique_segments = [1, 4, 7, 8]
    for u in unique_segments:
        letter_mappings[df_str_len == DISPLAY.loc[u].sum()] = u

    # 4 is part of 9
    four = _find_letters_representing_string_length(df_notes, df_str_len, 4)
    letter_mappings[
        (df_str_len == DISPLAY.loc[9].sum())
        & (
            df_notes.applymap(lambda x: set(x))
            .subtract(four.apply(lambda x: set(x)), axis=0)
            .applymap(lambda x: len(x))
            > 0
        )
    ] = 9

    # 1 is part of 0
    one = _find_letters_representing_string_length(df_notes, df_str_len, 1)
    letter_mappings[
        (df_str_len == DISPLAY.loc[0].sum())
        & (
            df_notes.applymap(lambda x: set(x))
            .subtract(one.apply(lambda x: set(x)), axis=0)
            .applymap(lambda x: len(x))
            > 0
        )
    ] = 0

    # otherwise its 6
    letter_mappings[df_str_len == DISPLAY.loc[6].sum()] = 6

    # 5 is part of 6
    five = _find_letters_representing_string_length(df_notes, df_str_len, 5)
    letter_mappings[
        (df_str_len == DISPLAY.loc[5].sum())
        & (
            df_notes.applymap(lambda x: set(x))
            .subtract(five.apply(lambda x: set(x)), axis=0)
            .applymap(lambda x: len(x))
            > 0
        )
    ] = 6

    # 1 is part of 3
    five = _find_letters_representing_string_length(df_notes, df_str_len, 5)
    letter_mappings[
        (df_str_len == DISPLAY.loc[3].sum())
        & (
            df_notes.applymap(lambda x: set(x))
            .subtract(one.apply(lambda x: set(x)), axis=0)
            .applymap(lambda x: len(x))
            > 0
        )
    ] = 3

    letter_mappings[df_str_len == DISPLAY.loc[5].sum()] = 2

    return letter_mappings
