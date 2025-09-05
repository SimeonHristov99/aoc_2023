def parse_input(filename: str) -> list[list[str]]:
    patterns = []
    with open(filename, 'r') as fp:
        patterns = fp.read()
    patterns = [pattern.split() for pattern in patterns.split('\n\n')]
    return patterns


def part1(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day_template/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day_template/input.txt")}')


if __name__ == '__main__':
    main()
