def predict(xs: list[int]) -> int:
    if all(x == 0 for x in xs):
        return 0
    return xs[-1] + predict([y - x for x, y in zip(xs, xs[1:])])


def part1(filename: str) -> int:
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day09/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day09/input.txt")}')

    print(f'Part 2, Sample: {part2("aoc_2023/day09/sample.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day09/input.txt")}')


if __name__ == '__main__':
    main()
