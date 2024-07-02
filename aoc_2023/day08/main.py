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


def part1(filename: str) -> int:
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day08/sample1.txt")}')  # 2
    print(f'Part 1, Sample: {part1("aoc_2023/day08/sample2.txt")}')  # 6
    # print(f'Part 1, Input: {part1("aoc_2023/day08/input.txt")}')

    # print(f'Part 2, Sample: {part2("aoc_2023/day08/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day08/input.txt")}')


if __name__ == '__main__':
    main()
