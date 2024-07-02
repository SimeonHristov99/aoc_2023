def parse_input(filename: str) -> tuple[str, dict[str, tuple[str, str]]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    directions = lines[0]
    map_ = {
        start_node: tuple(children[1:-1].split(', '))
        for line in lines[2:]
        for start_node, children in [line.split(' = ')]
    }
    return directions, map_


def num_steps(directions: str, map_: dict[str, tuple[str, str]]) -> int:
    pos = 'AAA'
    directions_idxs = [
        0 if direction == 'L' else 1 for direction in directions
    ]
    len_directions_idxs = len(directions_idxs)
    num_steps = 0
    while pos != 'ZZZ':
        pos = map_[pos][directions_idxs[num_steps % len_directions_idxs]]
        num_steps += 1
        if pos == 'ZZZ':
            break
    return num_steps


def part1(filename: str) -> int:
    directions, map_ = parse_input(filename)
    return num_steps(directions, map_)


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day08/sample1.txt")}')  # 2
    print(f'Part 1, Sample: {part1("aoc_2023/day08/sample2.txt")}')  # 6
    print(f'Part 1, Input: {part1("aoc_2023/day08/input.txt")}')  # 16409

    # print(f'Part 2, Sample: {part2("aoc_2023/day08/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day08/input.txt")}')


if __name__ == '__main__':
    main()
