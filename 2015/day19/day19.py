import re
from pathlib import Path

import pandas as pd
from utils_day19 import MEDICINE, compute_distinct_molecules

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> tuple[pd.DataFrame, str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
        rules = content[:-2]
        input_string = content[-1]
    df = pd.DataFrame([r.split(" => ") for r in rules], columns=["input", "output"])
    return df, input_string


def compute_num_distinct_molecules(rules: pd.DataFrame, medicine: str) -> int:
    """
    finds the number of distinct molecules under substitution rules
    """
    unique_strings = compute_distinct_molecules(rules, medicine)
    number = len(unique_strings)
    print(f"Q1 number: {number}")
    return number


def compute_steps_required_to_make_medicine(medicine_string: str) -> int:
    """
    naive A* search algorithm takes far too long so have used this
    https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/?utm_source=share&utm_medium=web2x&context=3
    all rules are of the form:
    * e -> XX or X -> XX (where X is not Rn/Y/Ar)
    * X => X Rn X Ar | X Rn X Y X Ar | X Rn X Y X Y X Ar
      or equivalently X => X(X) | X(X,X) | X(X,X,X)
    """
    # find all elements or electrons in medicine
    num_elements = len(re.findall(rf"{MEDICINE}|e", medicine_string))

    # create set of elements that follow above rules
    # dictionary of form element: (score, count)
    # Rn and Ar essentially subtract 1 extra element i.e. X(X) => X
    # Y allows for 2 extra to be removed i.e. X(X,X) => X
    special_elements = dict(
        Ar=(1, medicine_string.count("Ar")),
        Rn=(1, medicine_string.count("Rn")),
        Y=(2, medicine_string.count("Y")),
    )

    # if no special elements present then steps is the number of elements
    steps = num_elements

    # if any of these elements are present then calculate steps
    if any(element in special_elements.keys() for element in medicine_string):
        steps -= sum([e[0] * e[1] for e in special_elements.values()]) + 1

    print(f"Q2 steps: {steps}")
    return steps


if __name__ == "__main__":
    rules, medicine_string = read_data("data_day19.txt")
    # compute_num_distinct_molecules(rules, medicine_string)
    compute_steps_required_to_make_medicine(medicine_string)
