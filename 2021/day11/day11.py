from pathlib import Path

_file_location = Path(__file__).resolve()
_data_path = _file_location.parent


def read_data(filename: str) -> list[str]:
    with open(_data_path / filename) as f:
        content = f.read().splitlines()
    return content


if __name__ == "__main__":
    energies = read_data("data_day11.txt")
