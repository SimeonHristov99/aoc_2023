import queue


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
    generated = []
    generated.append(('', 0))

    for pat in pattern:
        new = []
        for (gen, br_idx) in generated:
            if pat == '?':
                if br_idx <= len(num_broken) and len(pattern) > 1:
                    new.append((gen + '.', br_idx))

                if '#' not in gen and num_broken[br_idx] == 1:
                    new.append((gen + '#', br_idx + 1))
                elif '#' not in gen:
                    new.append((gen + '#', br_idx))
                elif br_idx < len(
                        num_broken) and (gen.split('.')[-1]).count('#') + 1 == num_broken[br_idx]:
                    new.append((gen + '#', br_idx + 1))
                elif br_idx < len(
                        num_broken) and (gen.split('.')[-1]).count('#') + 1 < num_broken[br_idx]:
                    new.append((gen + '#', br_idx))
            elif pat == '#':
                if br_idx < len(
                        num_broken) and (gen.split('.')[-1]).count('#') + 1 == num_broken[br_idx]:
                    new.append((gen + '#', br_idx + 1))
                elif br_idx < len(
                        num_broken) and (gen.split('.')[-1]).count('#') + 1 < num_broken[br_idx]:
                    new.append((gen + '#', br_idx))

        generated = new

    return len(generated)


def expand(pattern: str, num_broken: list[int], factor: int) -> tuple[str, list[int]]:
    return ('?'.join([pattern] * factor), num_broken * factor)


def total_combinations(lines: list[tuple[str, list[int]]], expand_factor: int) -> int:
    result = 0
    for pattern, num_broken in lines:
        pattern, num_broken = expand(pattern, num_broken, expand_factor)
        result += get_num_combinations(pattern, num_broken)
    return result


def part1(filename: str) -> int:
    return total_combinations(parse(filename), 1)
