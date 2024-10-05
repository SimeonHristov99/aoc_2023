from __future__ import annotations


def get_lines(filename: str) -> list[str]:
    """
    Parses the lines of a text file.

    Args:
        filename (str): Path to the file for which to return the lines.

    Returns:
        list[str]: A list in which each element is a
            string representing the contents of each line in the provided file.
    """
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def parse_numbers(inp: str) -> list[int]:
    return [int(n) for n in inp.split()]


def get_seeds_and_maps(lines: list[str]):
    seeds = parse_numbers(lines[0].split(': ')[-1])

    maps = []
    current_map = {}
    for line in lines[2:]:
        if 'map' in line:
            continue
        elif len(line) > 0:
            destination_start, source_start, length = parse_numbers(line)
            current_map[destination_start] = (source_start, length)
        elif len(line) == 0:
            current_map = dict(current_map.items())
            maps.append(current_map)
            current_map = {}

    return seeds, maps


def move(destination: tuple[int, int], mapping: tuple[int, int],
         line: tuple[int, int]) -> tuple[tuple[int, int] | None, list[tuple[int, int]]]:
    (map_start, map_end) = mapping
    (destination_start, destination_end) = destination
    (line_start, line_end) = line

    if line_start <= map_start <= line_end <= map_end:
        # overlap to the right of line
        done = (destination_start, destination_start + line_end - map_start)

        if line_start == map_start:
            return done, []

        leftover = [(line_start, map_start - 1)]
        return done, leftover

    if map_start <= line_start <= map_end <= line_end:
        # overlap to the left of line
        done = (destination_start + line_start - map_start, destination_end)

        if map_end == line_end:
            return done, []

        leftover = [(map_end + 1, line_end)]
        return done, leftover

    if line_start <= map_start < map_end <= line_end:
        # overlap in the middle
        done = (destination_start, destination_end)
        leftover = [(line_start, map_start - 1), (map_end + 1, line_end)]

        if line_start == map_start and map_end == line_end:
            return done, []

        if line_start == map_start:
            return done, leftover[1]

        if map_end == line_end:
            return done, leftover[0]

        return done, leftover

    if map_start <= line_start <= line_end <= map_end:
        # map contains line
        done = (destination_start + line_start - map_start, destination_end - (map_end - line_end))
        return done, []

    # no overlap
    return None, [(line_start, line_end)]


def apply_map(map_: dict[int, tuple[int, int]], line: tuple[int, int]) -> set[tuple[int, int]]:
    dones = set()
    to_processs = [line]
    seen = set()

    for destination_start, (map_start, map_length) in map_.items():
        leftovers = []
        for to_process in to_processs:
            destination = (destination_start, destination_start + map_length - 1)
            mapping = (map_start, map_start + map_length - 1)
            done, leftover = move(destination, mapping, to_process)
            if done:
                dones.add(done)
                seen.add(to_process)
            if to_process != mapping:
                dones.update(leftover)
                leftovers.extend(leftover)
        to_processs = leftovers

    dones.update(to_processs)
    dones = dones - seen

    return dones


def almanac(maps: list[dict[int, tuple[int, int]]], line: tuple[int, int]) -> set[tuple[int, int]]:
    done = set()
    num_maps = len(maps)
    lines = {line}
    for idx, map_ in enumerate(maps):
        new_ranges = set()
        for range_ in lines:
            new_ranges |= apply_map(map_, range_)
            if idx + 1 == num_maps:
                done |= new_ranges
        lines = new_ranges
    return done


def part1(filename: str) -> int:
    seeds, maps = get_seeds_and_maps(get_lines(filename))
    acc = float('inf')

    for seed in seeds:
        acc = min(acc, almanac(maps, (seed, seed)).pop()[0])

    return int(acc)


def part2(filename: str) -> int:
    seed_ranges, maps = get_seeds_and_maps(get_lines(filename))
    it = iter(seed_ranges)
    lines = list(zip(it, it))

    acc = float('inf')

    for (line_start, line_length) in lines:
        results = almanac(maps, (line_start, line_start + line_length - 1))
        locations = [coords[0] for coords in results]
        acc = min(acc, min(locations))

    return int(acc)


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day05/sample.txt")}')  # 35
    print(f'Part 1, Input: {part1("aoc_2023/day05/input.txt")}')  # 323142486

    print(f'Part 2, Sample: {part2("aoc_2023/day05/sample.txt")}')  # 46
    print(f'Part 2, Input: {part2("aoc_2023/day05/input.txt")}')  # 79874951


if __name__ == '__main__':
    main()
