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


def get_num_combinations(pattern: str, num_broken: list[int]) -> int:

    def helper(idx, result):
        if idx >= len(pattern):
            return is_working_combination(result, num_broken)
        if pattern[idx] == '?':
            return helper(idx + 1, result + '.') + helper(idx + 1, result + '#')
        return helper(idx + 1, result + pattern[idx])

    return helper(0, '')
