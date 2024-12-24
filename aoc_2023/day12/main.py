def parse(filename: str) -> list[tuple[str, list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((input_string, [int(grp) for grp in groups.split(',')]))
    return result


def is_working_combination(substring: str, groups: list[int]) -> bool:
    return [subgroup.count('#') for subgroup in substring.split('.') if subgroup] == groups


def is_valid(result: str, num_broken: list[int]) -> bool:
    groups_so_far = [subgroup.count('#') for subgroup in result.rstrip('#').split('.') if subgroup]
    return groups_so_far == num_broken[:len(groups_so_far)]


def get_num_combinations(pattern: str, num_broken: list[int]) -> int:

    def helper(idx, result):
        if idx >= len(pattern):
            return is_working_combination(result, num_broken)

        if not is_valid(result, num_broken):
            return 0

        if pattern[idx] == '?':
            return helper(idx + 1, result + '.') + helper(idx + 1, result + '#')
        return helper(idx + 1, result + pattern[idx])

    return helper(0, '')


def part1(filename: str) -> int:
    lines = parse(filename)
    result = 0
    for pattern, num_broken in lines:
        result += get_num_combinations(pattern, num_broken)
    return result
