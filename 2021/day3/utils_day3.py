import pandas as pd

FAVOURED = dict(most_common="1", least_common="0")
NAME = "binary"


def _convert_str_to_bool(df: pd.DataFrame) -> pd.DataFrame:
    """
    convert string datatype to boolean via integer
    """
    return df.astype(int).astype(bool)


def _convert_bool_to_str(df: pd.DataFrame) -> pd.DataFrame:
    """
    convert boolean datatype to string via integer
    """
    return df.astype(int).astype(str)


def create_df_of_one_and_zero(df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    read in str df and create columns with one and zero
    """
    return df[name].str.split("", expand=True).iloc[:, 1:-1]


def find_most_common(df: pd.DataFrame) -> pd.DataFrame:
    """
    finds the most common values in dataframe
    """
    return df.mode()


def find_least_common(df: pd.DataFrame) -> int:
    """
    finds the least common values in dataframe,
    this leverages boolean logic to find the anti mode
    """
    return _convert_bool_to_str(~_convert_str_to_bool(find_most_common(df)))


def extract_rate_as_int(df: pd.DataFrame) -> int:
    """
    extract rate as integer from dataframe
    """
    base = 2
    list_of_ints = _convert_bool_to_str(df).iloc[0].to_list()
    binary_str = "".join(list_of_ints)
    return int(binary_str, base)


def _modified_mode_for_duplicates(df: pd.DataFrame, favoured: str) -> str:
    """
    in the event that there are multiple modal values then pick the favoured one
    """
    return df.values[0] if len(df) == 1 else favoured


def loop_through_df_to_compute_rates(df: pd.DataFrame, favoured: str) -> int:
    """
    loop through the dataframe and find the mode and then compute the rate
    """
    for i in range(df.shape[1]):
        if df.shape[0] == 1:
            # require at least one row
            break
        df_column = df.iloc[:, i]
        common = (
            _modified_mode_for_duplicates(find_most_common(df_column), "1")
            if favoured == "1"
            else _modified_mode_for_duplicates(find_least_common(df_column), "0")
        )
        matching = df_column == common
        df = df.loc[matching].reset_index(drop=True)
    return extract_rate_as_int(df)
