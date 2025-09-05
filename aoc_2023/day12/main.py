def parse(filename: str) -> list[tuple[str, list[int]]]:
    with open(filename, 'r') as fp:
        lines = fp.read().splitlines()
    result = []
    for line in lines:
        input_string, groups = line.split()
        result.append((input_string, [int(grp) for grp in groups.split(',')]))
    return result


def get_num_combinations(pattern: str, num_broken: list[int], cache: dict | None = None) -> int:
    if pattern == '':
        return 1 if num_broken == [] else 0

    if num_broken == []:
        return 0 if '#' in pattern else 1

    key = (pattern, tuple(num_broken))
    if cache is not None and key in cache:
        return cache[key]

    count = 0

    if pattern[0] == '.' or pattern[0] == '?':
        # treating the '?' as '.'
        count += get_num_combinations(pattern[1:], num_broken, cache)

    if ((pattern[0] == '#' or pattern[0] == '?') and len(pattern) >= num_broken[0]
            and '.' not in pattern[:num_broken[0]]
            and (len(pattern) == num_broken[0] or pattern[num_broken[0]] != '#')):
        # treating the '?' as '#'
        count += get_num_combinations(pattern[num_broken[0] + 1:], num_broken[1:], cache)

    if cache is not None:
        cache[key] = count
    return count


def part1(filename: str) -> int:
    lines = parse(filename)
    result = 0
    for pattern, num_broken in lines:
        result += get_num_combinations(pattern, num_broken)
    return result


def part2(filename: str) -> int:
    lines = parse(filename)
    result = 0
    cache: dict[tuple[str, tuple[int]], int] = {}
    for pattern, num_broken in lines:
        pattern = '?'.join([pattern for _ in range(5)])
        num_broken *= 5
        result += get_num_combinations(pattern, num_broken, cache)
    return result
