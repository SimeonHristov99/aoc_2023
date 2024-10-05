from typing import List, Tuple


def parse_input(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return [[c for c in line] for line in lines]


def find_start(pipe_map: List[List[str]]) -> Tuple[int, int]:
    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[0])):
            if pipe_map[i][j] == 'S':
                return (i, j)
    return (-1, -1)


def part1(filename: str) -> int:
    print(parse_input(filename))
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("./aoc_2023/day10_new/sample.txt")}')
    # print(f'Part 1, Input: {part1("input.txt")}')

    # print(f'Part 2, Sample: {part2("./aoc_2023/day10_new/sample.txt")}')
    # print(f'Part 2, Input: {part2("input.txt")}')


if __name__ == '__main__':
    main()
