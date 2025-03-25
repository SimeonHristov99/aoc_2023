def parse(filename: str) -> list[tuple[str, list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((input_string, [int(grp) for grp in groups.split(',')]))
    return result


def get_num_combinations(pattern: str, num_broken: list[int]) -> int:
    if pattern == '':
        return 1 if num_broken == [] else 0

    if num_broken == []:
        return 0 if '#' in pattern else 1

    count = 0

    if pattern[0] == '.' or pattern[0] == '?':
        # treating the '?' as '.'
        count += get_num_combinations(pattern[1:], num_broken)

    if ((pattern[0] == '#' or pattern[0] == '?') and len(pattern) >= num_broken[0]
            and '.' not in pattern[:num_broken[0]]
            and (len(pattern) == num_broken[0] or pattern[num_broken[0]] != '#')):
        # treating the '?' as '#'
        count += get_num_combinations(pattern[num_broken[0] + 1:], num_broken[1:])

    return count


def part1(filename: str) -> int:
    lines = parse(filename)
    result = 0
    for pattern, num_broken in lines:
        result += get_num_combinations(pattern, num_broken)
    return result
