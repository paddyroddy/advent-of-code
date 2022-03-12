from collections import defaultdict

import pandas as pd

FOUND_ONCE = 1


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
    *,
    visit_small_twice: bool = False,
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
            if new_point.islower():
                if new_point not in current_path:
                    recursive_check_for_paths(
                        connections,
                        new_point,
                        target,
                        visit_small_twice=visit_small_twice,
                        current_path=new_path,
                        all_paths=all_paths,
                    )
                elif visit_small_twice and new_point != "start":
                    recursive_check_for_paths(
                        connections,
                        new_point,
                        target,
                        visit_small_twice=False,
                        current_path=new_path,
                        all_paths=all_paths,
                    )
            else:
                recursive_check_for_paths(
                    connections,
                    new_point,
                    target,
                    visit_small_twice=visit_small_twice,
                    current_path=new_path,
                    all_paths=all_paths,
                )

    return all_paths
