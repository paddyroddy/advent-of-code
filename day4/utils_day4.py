def convert_numbers_to_ints(numbers: str) -> list[int]:
    """
    the called numbers are read in as a string originally
    """
    return list(map(int, numbers.split(",")))
