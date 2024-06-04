from __future__ import annotations

from collections import defaultdict

from aoc_2023 import utils


def parse_numbers(inp: str) -> list[int]:
    return [int(n) for n in inp.split()]


def get_seeds_mappings(lines: list[str]) -> tuple[list[int], defaultdict]:
    seeds = parse_numbers(lines[0].split(': ')[-1])

    mappings = defaultdict(list)

    name = ''
    for line in lines[2:]:
        if 'map' in line:
            name = line.split()[0]
        elif len(line) > 0:
            destination_start, source_start, length = parse_numbers(line)
            mappings[name].append((destination_start, source_start, length))

    return seeds, mappings


def map_value(mappings: list[tuple[int, int, int]], seed: int) -> int:
    for destination, source, size in mappings:
        if source <= seed < source + size:
            return destination + seed - source
    return seed


def get_location(mappings: defaultdict, seed: int):
    for _, maps in mappings.items():
        seed = map_value(maps, seed)
    return seed


def part1(filename: str) -> int:
    min_loc = float('inf')
    seeds, mappings = get_seeds_mappings(utils.get_lines(filename))
    for seed in seeds:
        min_loc = min(min_loc, get_location(mappings, seed))
    return int(min_loc)


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day05/sample.txt")}')  # 35
    print(f'Part 1, Input: {part1("aoc_2023/day05/input.txt")}')  # 323142486

    # print(f'Part 2, Sample: {part2("aoc_2023/day05/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day05/input.txt")}')


if __name__ == '__main__':
    main()
