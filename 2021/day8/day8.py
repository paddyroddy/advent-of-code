import re
from pathlib import Path

import pandas as pd
from utils_day8 import create_columns

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return pd.DataFrame(
        [re.split(r"\s\|\s|\s", c) for c in content], columns=create_columns(content)
    )


if __name__ == "__main__":
    notes = read_data("dummy_day8.txt")
