def parse(filename: str) -> list[tuple[list[str], list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((list(input_string), [int(grp) for grp in groups.split(',')]))
    return result


def is_working_combination(substring: str, groups: list[int]) -> bool:
    return [subgroup.count('#') for subgroup in substring.split('.') if subgroup] == groups


def get_num_combinations(pattern: list[str], num_broken: list[int]) -> int:

    def helper(idx, result):
        if idx >= len(pattern):
            print(result)
            return is_working_combination(result, num_broken)

        if pattern[idx] == '?':
            s1 = helper(idx + 1, result + '.')
            s2 = helper(idx + 1, result + '#')
            return s1 + s2

        return helper(idx + 1, result + pattern[idx])

    return helper(0, '')
