from typing import List

def parse_input(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return [[c for c in line] for line in lines]

def part1(filename: str) -> int:
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("sample.txt")}')
    print(f'Part 1, Input: {part1("input.txt")}')

    print(f'Part 2, Sample: {part2("sample.txt")}')
    print(f'Part 2, Input: {part2("input.txt")}')


if __name__ == '__main__':
    main()
