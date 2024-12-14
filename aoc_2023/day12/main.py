def parse(filename: str) -> list[tuple[list[str], list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((list(input_string), [int(grp) for grp in groups.split(',')]))
    return result


def create_combinations(num_broken, result, idx_start, idx_current, it_num_broken,
                        it_pattern) -> int:
    next_group = next(it_num_broken, None)
    if not next_group and idx_current > len(num_broken):
        return 1
    if next_group and idx_current > len(num_broken):
        return 0
    return 2


def get_num_combinations(pattern: list[str], num_broken: list[int]) -> int:
    return 1
