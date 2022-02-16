ILLEGAL_CHARS_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
MATCHING_BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def find_if_line_corrupted(line: str) -> bool:
    """
    checks if the line is corrupted
    """
    # initialise the stack of characters
    stack = list()

    # create list of opening and closings
    opening = list(MATCHING_BRACKETS.keys())
    closing = list(MATCHING_BRACKETS.values())

    # loop over line
    for char in line:
        if char in opening:
            stack.append(char)
        if char in closing:
            candidate = stack.pop()


def compute_score_from_chars(char_count: dict[str, int]) -> int:
    """
    computes the score from the given charachter count
    """
    individual_char_scores = {
        k: v * ILLEGAL_CHARS_SCORES[k] for k, v in char_count.items()
    }
    return sum(individual_char_scores.values())
