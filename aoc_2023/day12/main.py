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

def simplify(pattern: str, num_broken: list[int]) -> tuple[str, list[int]]:
    simplified_pattern = pattern
    simplified_num_broken = num_broken

    continue_loop = True
    while continue_loop:
        continue_loop = False
        simplified_pattern_len = len(simplified_pattern)
        simplified_num_broken_result = []

        for current_num_broken in simplified_num_broken:
            subpattern = '#' * current_num_broken
            subpattern_len = len(subpattern)
            print('\t', f'Searching for {subpattern}:')
            matched = False
            for i in range(simplified_pattern_len):
                candidate_end_idx = i+subpattern_len
                candidate = simplified_pattern[i:candidate_end_idx]

                if len(candidate) < subpattern_len:
                    continue

                print('\t\t', candidate)
                if (candidate == subpattern
                    and (i == 0 or simplified_pattern[i - 1] == '.')
                    and (candidate_end_idx == simplified_pattern_len or simplified_pattern[candidate_end_idx] == '.')):
                    print('\t\t\t', 'Matches!')
                    matched = True
                    continue_loop = True
                    break

            if not matched:
                simplified_num_broken_result.append(current_num_broken)

        simplified_num_broken = simplified_num_broken_result

        print('\t', f'{simplified_pattern=}')
        print('\t', f'{simplified_num_broken=}')

    return simplified_pattern, simplified_num_broken

def part1(filename: str) -> int:
    lines = parse(filename)
    result = 0
    # full_output_str = ''
    print()
    for pattern, num_broken in lines[:3]:
        print(pattern, num_broken)
        result += get_num_combinations(pattern, num_broken)
        simplified_pattern, simplified_num_broken = simplify(pattern, num_broken)
        print('\n')

    # print(full_output_str)

    return result
