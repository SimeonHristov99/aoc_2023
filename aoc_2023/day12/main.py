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
    full_output_str = ''
    for pattern, num_broken in lines:
        res_current = get_num_combinations(pattern, num_broken)
        result += res_current

        num_broken_as_pattern = '.'.join(['#'*num for num in num_broken])
        bin_pattern = ''.join(['1' if pat == '#' else ('0' if pat == '.' else pat) for pat in pattern])
        bin_minimum = ''.join(['1' if pat == '1' else '0' for pat in bin_pattern])
        decimal_minimum = str(int(bin_minimum, 2))
        bin_maximum = ''.join(['0' if pat == '0' else '1' for pat in bin_pattern])
        decimal_maximum = str(int(bin_maximum, 2))
        decimal_diff = str(int(decimal_maximum) - int(decimal_minimum))

        full_output_str += '\n' + '=> '.join([
            pattern.ljust(25),
            num_broken_as_pattern.ljust(20),
            bin_pattern.ljust(25),
            bin_minimum.ljust(25),
            decimal_minimum.ljust(10),
            bin_maximum.ljust(25),
            decimal_maximum.ljust(10),
            decimal_diff.ljust(10),
            str(res_current),
        ])
    
    print()
    print(full_output_str)

    with open('input_visualized.txt', 'w') as filep:
        filep.write(full_output_str)

    return result
