def parse(filename: str) -> list[tuple[str, list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((input_string, [int(grp) for grp in groups.split(',')]))
    return result

def get_num_combinations(pattern: str, num_broken: list[int]):
    return 1


def part1(filename: str) -> int:
    lines = parse(filename)
    result = 0
    for pattern, num_broken in lines:
        result += get_num_combinations(pattern, num_broken)
    return result
