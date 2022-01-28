import re

import pandas as pd

MEDICINE = r"[A-Z][a-z]?"


def _swap_molecule_in_string(
    input_string: str, position: int, old_molecule: str, new_molecule: str
) -> str:
    """
    swaps a molecule at given position in a string
    """
    return (
        input_string[:position]
        + new_molecule
        + input_string[position + len(old_molecule) :]
    )


def _create_list_of_elements(medicine_string: str) -> list[str]:
    """
    the input string is a combination of chemical elements, this function
    splits this string up into a list of the consituent elements
    """
    return re.findall(MEDICINE, medicine_string)


def _find_matching_molecules(
    medicine_string: str, df_rules: pd.DataFrame, position: int, old_molecule: str
) -> set[str]:
    """
    find the new molecules that replace the old ones
    """
    matched_rule = df_rules["input"] == old_molecule
    replaced_elements = df_rules.loc[matched_rule, "output"]
    return {
        _swap_molecule_in_string(medicine_string, position, old_molecule, new_molecule)
        for new_molecule in replaced_elements
    }


def compute_distinct_molecules(rules: pd.DataFrame, medicine_string: str) -> set[str]:
    """
    performs the molecule replacements and then creates a set of the distinct molecules
    """
    # initialise position of molecule in string
    position = 0

    # initialise set of molecules
    unique_strings = set()

    # create list of elements in input string
    elements_list = _create_list_of_elements(medicine_string)

    # loop through elements in list
    for element in elements_list:
        new_strings = _find_matching_molecules(
            medicine_string, rules, position, element
        )
        unique_strings |= new_strings
        position += len(element)
    return unique_strings
