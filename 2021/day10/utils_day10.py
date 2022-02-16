ILLEGAL_CHARS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_if_line_corrupted(line: str) -> bool:
    """
    checks if the line is corrupted
    """
    stack: list[str] = list()
    for char in line:
        if char in ILLEGAL_CHARS:
            if not stack:
                return True
            else:
                if ILLEGAL_CHARS[char] == stack.pop():
                    continue
                else:
                    return True
        else:
            stack.append(char)
    return False


def compute_score_from_chars(char_count: dict[str, int]) -> int:
    """
    computes the score from the given charachter count
    """
    individual_char_scores = {k: v * ILLEGAL_CHARS[k] for k, v in char_count.items()}
    return sum(individual_char_scores.values())
