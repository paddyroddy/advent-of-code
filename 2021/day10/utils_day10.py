from collections import Counter

CLOSING_CHARS_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
ILLEGAL_CHARS_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
MATCHING_BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}
NOT_CORRUPTED = ""
SCORE_MULTIPLIER = 5


def _compute_intermediate_completion_score(curr_score: int, new_char: str) -> int:
    """
    helper function to compute the new score after adding a new character
    """
    return (
        SCORE_MULTIPLIER * curr_score
        + CLOSING_CHARS_SCORES[MATCHING_BRACKETS[new_char]]
    )


def check_if_line_corrupted(line: str) -> tuple[str, list[str]]:
    """
    checks if the line is corrupted, if so return offending character
    """
    # initialise the stack of characters
    stack: list[str] = list()

    # loop through line
    for char in line:
        if char in MATCHING_BRACKETS.keys():
            # opening character, add to stack
            stack.append(char)
            continue
        if char in MATCHING_BRACKETS.values():
            # closing character, check if as expected
            candidate = stack.pop()
            if char != MATCHING_BRACKETS[candidate]:
                return char, stack
    return NOT_CORRUPTED, stack


def compute_error_score_from_chars(char_count: Counter) -> int:
    """
    computes the score from the given charachter count
    """
    individual_char_scores = {
        k: v * ILLEGAL_CHARS_SCORES[k] for k, v in char_count.items()
    }
    return sum(individual_char_scores.values())


def complete_the_lines_with_score(stack: list[str]) -> int:
    """
    for an incomplete line work out what characters are required
    to complete it and compute the completion score
    """
    # initialise the score
    score = 0

    # loop through the stack reducing the size
    while len(stack) > 0:
        char = stack.pop()
        score = _compute_intermediate_completion_score(score, char)
    return score
