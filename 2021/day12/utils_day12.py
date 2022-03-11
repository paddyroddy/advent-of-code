from collections import defaultdict

import pandas as pd


def _valid_new_point(point: str, visited: list[str]) -> bool:
    """
    check if the given point is a valid new point
    """
    return point.isupper() or point not in visited


def convert_df_to_dict(df: pd.DataFrame) -> dict[str, list[str]]:
    """
    convert the given dataframe to a dictionary with mappings
    in both direction from each set of nodes
    """
    # initialise output
    connections: dict[str, list[str]] = defaultdict(list)

    # loop over dataframe
    for _, row in df.iterrows():
        left, right = row
        connections[left].append(right)
        connections[right].append(left)
    return connections


def recursive_check_for_paths(
    connections: dict[str, list[str]],
    point: str,
    target: str,
    current_path: list[str] = [],
    all_paths: list[str] = [],
) -> list[str]:
    """
    recursively loop through paths and find the total count
    """
    # create copy of new path each time function called
    new_path = current_path + [point]

    if point == target:
        all_paths.append(new_path[:])  # type: ignore
    else:
        for new_point in connections[point]:
            if _valid_new_point(new_point, new_path):
                recursive_check_for_paths(
                    connections, new_point, target, new_path, all_paths
                )

    return all_paths
