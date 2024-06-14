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
            current_map[source_start] = (destination_start, length)
        elif len(line) == 0:
                current_map = dict(sorted(current_map.items(), key=lambda kv: kv[0]))
                maps.append(current_map)
                current_map = {}

    return seeds, maps


def get(map, seed):
    if seed in map:
        return map[seed][0]

    c_map_ks = list(map.keys())
    for k1, k2 in zip(c_map_ks, c_map_ks[1:]):
        if k1 <= seed <= k2:
            destination_start, length = map[k1]
            return destination_start + seed - k1 if seed <= k1 + length else seed

    return map[k2][0] + seed - k2 if k2 <= seed <= k2 + map[k2][1] else seed


def part1(filename: str) -> int:
    seeds, maps = get_seeds_and_maps(get_lines(filename))

    locations = []
    
    for seed in seeds:
        for c_map in maps:
            seed = get(c_map, seed)
        
        locations.append(seed)

    return min(locations)


def part2(filename: str) -> int:
    seed_ranges, maps = get_seeds_and_maps(get_lines(filename))

    ranges = [tuple(seed_ranges[i:i+2]) for i in range(0, len(seed_ranges), 2)]

    locations = []
    
    for seed, range_length in ranges:
        seed_to = seed
        for c_map in maps:
            seed_from = seed_to
            seed_to = get(c_map, seed_from)
        locations.append(seed_to)
        
        for _ in range(range_length - 1):
            seed_from += 1
            locations.append(get(c_map, seed_from))

    return min(locations)


def main() -> None:
    # print(f'Part 1, Sample: {part1("aoc_2023/day05/sample.txt")}')  # 35
    # print(f'Part 1, Input: {part1("aoc_2023/day05/input.txt")}')  # 323142486

    print(f'Part 2, Sample: {part2("aoc_2023/day05/sample.txt")}')  # 46
    # print(f'Part 2, Input: {part2("aoc_2023/day05/input.txt")}')


if __name__ == '__main__':
    main()
