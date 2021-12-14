import pandas as pd


def create_df_of_one_and_zero(df: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    read in str df and create columns with one and zero
    """
    return df[name].str.split("", expand=True).iloc[:, 1:-1]


def convert_str_to_bool(df: pd.DataFrame) -> pd.DataFrame:
    """
    convert string datatype to boolean via integer
    """
    return df.astype(int).astype(bool)


def convert_bool_to_str(df: pd.DataFrame) -> pd.DataFrame:
    """
    convert boolean datatype to string via integer
    """
    return df.astype(int).astype(str)


def extract_rate_as_int(df: pd.DataFrame) -> pd.DataFrame:
    """
    extract rate as integer from dataframe
    """
    list_of_ints = convert_bool_to_str(df).iloc[0].to_list()
    binary_str = "".join(list_of_ints)
    return int(binary_str, 2)
