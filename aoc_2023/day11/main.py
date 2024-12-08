def parse(filepath: str) -> list[list[str]]:
    with open(filepath, 'r') as file_fp:
        lines = file_fp.read().splitlines()
    return [list(line) for line in lines]
