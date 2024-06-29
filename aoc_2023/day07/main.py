import enum
from typing import Counter


class CardType(enum.IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def parse_input(filename: str) -> dict[str, int]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    return {hand: int(bid) for line in lines for hand, bid in [line.split()]}


def card_type(hand: str) -> CardType:
    distribution = sorted(Counter(hand).values())

    match distribution:
        case [5]:
            return CardType.FIVE_OF_A_KIND
        case [1, 4]:
            return CardType.FOUR_OF_A_KIND
        case [2, 3]:
            return CardType.FULL_HOUSE
        case [1, 1, 3]:
            return CardType.THREE_OF_A_KIND
        case [1, 2, 2]:
            return CardType.TWO_PAIR
        case [1, 1, 1, 2]:
            return CardType.ONE_PAIR
        case _:
            return CardType.HIGH_CARD


def compare(hand1: str, hand2: str) -> int:
    type_lhs = card_type(hand1)
    type_rhs = card_type(hand2)

    if type_lhs < type_rhs:
        return -1

    if type_lhs > type_rhs:
        return 1

    for v1, v2 in zip(
        sorted(hand1, reverse=True), sorted(hand2, reverse=True)
    ):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1

    raise NotImplementedError(f'Cards are the same: {hand1}, {hand2}.')


def part1(filename: str) -> int:
    return 42


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day07/sample.txt")}')  # 6440
    # print(f'Part 1, Input: {part1("aoc_2023/day07/input.txt")}')  #

    # print(f'Part 2, Sample: {part2("aoc_2023/day07/sample.txt")}')  #
    # print(f'Part 2, Input: {part2("aoc_2023/day07/input.txt")}')  #


if __name__ == '__main__':
    main()
