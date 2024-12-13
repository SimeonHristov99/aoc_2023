def parse(filename: str) -> list[tuple[list[str], list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((list(input_string), [int(grp) for grp in groups.split(',')]))
    return result
