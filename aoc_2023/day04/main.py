from __future__ import annotations

from aoc_2023 import utils


def get_points(card: str) -> int:
    numbers_winning, numbers_have = card.split(': ')[1].split(' | ')
    numbers_winning_set = set(numbers_winning.split())
    numbers_have_set = set(numbers_have.split())
    numbers_have_winning = numbers_have_set & numbers_winning_set
    if not numbers_have_winning:
        return 0
    return 2**(len(numbers_have_winning) - 1)


def part1(filename: str) -> int:
    cards = utils.get_lines(filename)
    points = [get_points(card) for card in cards]
    return sum(points)


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day04/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day04/input.txt")}')

    # print(f'Part 2, Sample: {part2("aoc_2023/day04/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day04/input.txt")}')


if __name__ == '__main__':
    main()
