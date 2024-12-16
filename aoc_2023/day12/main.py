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

    def dfs(result, idx_start, idx_current, idx_groups, idx_springs) -> int:
        current_character = pattern[idx_springs] if idx_springs < len(pattern) else None
        if not current_character and idx_groups >= len(num_broken):
            return 1

        substring = result[idx_start:]
        state = get_state(substring, num_broken[idx_groups])

        if not current_character and state != 'full_group':
            return 0
        if state == 'full_group':
            return 1

        if current_character == '?' and state == 'full_group':
            return dfs(result + '.', idx_current + 1, idx_current + 2, idx_groups, idx_springs)
        if current_character == '?' and state == 'valid':
            return dfs(
                result + '.', idx_start, idx_current + 1, idx_groups, idx_springs + 1) + dfs(
                    result + '#', idx_start, idx_current + 1, idx_groups, idx_springs + 1)
        if current_character == '?':
            return 0
        if state == 'full_group' and substring[-1] != '#' and current_character != '#':
            return dfs(result + current_character, idx_current + 1, idx_current + 2, idx_groups,
                       idx_springs)
        if state == 'full_group' and substring[-1] == '#' and current_character == '#':
            return 0
        if state == 'valid':
            return dfs(result + current_character, idx_start, idx_current + 1, idx_groups,
                       idx_springs)

    return dfs('', 0, 1, 0, 0)
