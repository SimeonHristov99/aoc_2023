def parse(filename: str) -> list[tuple[list[str], list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((list(input_string), [int(grp) for grp in groups.split(',')]))
    return result


def get_state(substring: str, current_group: int) -> str:
    expected_content = '#' * current_group
    return 'full_group' if expected_content in substring else 'valid'


def get_num_combinations(pattern: list[str], num_broken: list[int]) -> int:

    def dfs(result, idx_start, idx_current, iter_groups, iter_springs) -> int:
        current_group = next(iter_groups, None)
        current_character = next(iter_springs, None)

        if not current_character and not current_group:
            return 1
        if not current_character and current_group:
            return 0

        substring = result[idx_start:idx_current]
        state = get_state(substring, current_group)

        if current_character == '?' and state == 'full_group':
            return dfs(result + '.', idx_current + 1, idx_current + 2, iter_groups, iter_springs)
        if current_character == '?' and state == 'valid':
            return dfs(
                result + '.', idx_current + 1, idx_current + 2, iter_groups, iter_springs) + dfs(
                    result + '#', idx_current + 1, idx_current + 2, iter_groups, iter_springs)
        if current_character == '?':
            return 0
        if state == 'full_group' and substring[-1] != '#' and current_character != '#':
            return dfs(result + current_character, idx_current + 1, idx_current + 2, iter_groups,
                       iter_springs)
        if state == 'full_group' and substring[-1] == '#' and current_character == '#':
            return 0
        if state == 'valid':
            return dfs(result + current_character, idx_current + 1, idx_current + 2, iter_groups,
                       iter_springs)

    return dfs('', 0, 1, iter(num_broken), iter(pattern))
