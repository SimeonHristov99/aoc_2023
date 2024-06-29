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


def is_five_of_a_kind(hand: str) -> bool:
    return len(set(hand)) == 1


def is_four_of_a_kind(hand: str) -> bool:
    return set(Counter(hand).values()) == {1, 4}


def is_full_house(hand: str) -> bool:
    return set(Counter(hand).values()) == {2, 3}


def is_three_of_a_kind(hand: str) -> bool:
    return sorted(Counter(hand).values()) == [1, 1, 3]


def is_two_pair(hand: str) -> bool:
    return sorted(Counter(hand).values()) == [1, 2, 2]


def is_one_pair(hand: str) -> bool:
    return sorted(Counter(hand).values()) == [1, 1, 1, 2]


def card_type(hand: str) -> CardType:
    if is_five_of_a_kind(hand):
        return CardType.FIVE_OF_A_KIND
    if is_four_of_a_kind(hand):
        return CardType.FOUR_OF_A_KIND
    if is_full_house(hand):
        return CardType.FULL_HOUSE
    if is_three_of_a_kind(hand):
        return CardType.THREE_OF_A_KIND
    if is_two_pair(hand):
        return CardType.TWO_PAIR
    if is_one_pair(hand):
        return CardType.ONE_PAIR
    return CardType.HIGH_CARD


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
