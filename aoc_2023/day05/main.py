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
            current_map = dict(
                sorted(current_map.items(), key=lambda kv: kv[0]),
            )
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
            if seed <= k1 + length:
                return destination_start + seed - k1
            return seed

    if k2 <= seed <= k2 + map[k2][1]:
        return map[k2][0] + seed - k2
    return seed


def part1(filename: str) -> int:
    seeds, maps = get_seeds_and_maps(get_lines(filename))

    locations = []

    for seed in seeds:
        for c_map in maps:
            seed = get(c_map, seed)

        locations.append(seed)

    return min(locations)


def step(to_process, line_start, line_end):
    diff = line_end[0] - line_start[0]

    if line_start[0] <= to_process[0] < to_process[1] <= line_start[1]:
        # interval contains source line
        done = (to_process[0] + diff, to_process[1] + diff)
        to_process = []
        return (done, to_process)

    if line_start[0] <= to_process[0]:
        # interval contains left part of source line, but not end
        done = (to_process[0] + diff, line_start[1] + diff)
        to_process = (line_start[1] + 1, to_process[1])
        return (done, to_process)

    if line_start[0] <= to_process[1]:
        # interval contains right part of source line, but not start
        done = (line_start[0] + diff, to_process[1] + diff)
        to_process = (to_process[0], line_start[0] - 1)
        return (done, to_process)

    if to_process[0] <= line_start[0] < line_start[1] <= to_process[1]:
        # interval is contained in source line
        to_process_before = (to_process[0], line_start[0] - 1)
        done_on_line = (line_start[0] + diff, line_start[1] + diff)
        to_process_after = (line_start[1] + 1, to_process[1])
        return (done_on_line, [to_process_before, to_process_after])

    # interval does not contained any part of source line
    return (None, [to_process])


def part2(filename: str) -> int:
    seed_ranges, maps = get_seeds_and_maps(get_lines(filename))
    it = iter(seed_ranges)
    ranges = list(zip(it, it))

    for range in ranges:
        to_process = [range]

        for map in maps:
            dones = []

            for dest_start, (source_start, length) in map.items():
                to_process_new = []
                for to_process_current in to_process:
                    done, to_pr = step(
                        to_process_current, source_start,
                        source_start + length - 1
                    )
                    to_process_new.append(to_pr)
                    if done:
                        dones.append(done)

            to_process.extend(dones)

    return 42


def move(
    destination: tuple[int, int], map_: tuple[int, int], line: tuple[int, int]
) -> tuple[tuple[int, int] | None, list[tuple[int, int]]]:
    (map_start, map_end) = map_
    (destination_start, destination_end) = destination
    (line_start, line_end) = line

    if line_start <= map_start <= line_end < map_end:
        # overlap to the right of line
        done = (destination_start, destination_start + line_end - map_start)
        leftover = [(line_start, map_start - 1)]
        return done, leftover

    # no overlap
    return None, [(line_start, line_end)]


def main() -> None:
    # print(f'Part 1, Sample: {part1("aoc_2023/day05/sample.txt")}')  # 35
    # print(f'Part 1, Input: {part1("aoc_2023/day05/input.txt")}')  # 323142486

    print(f'Part 2, Sample: {part2("aoc_2023/day05/sample.txt")}')  # 46
    # print(f'Part 2, Input: {part2("aoc_2023/day05/input.txt")}')


if __name__ == '__main__':
    main()
