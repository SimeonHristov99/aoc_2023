import enum
import functools
from collections import Counter


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


def card_type(hand: str, joker: bool = False) -> CardType:
    counts = Counter(hand)
    distribution = sorted(counts.values())

    match distribution:
        case [5]:
            return CardType.FIVE_OF_A_KIND
        case [1, 4]:
            if 'J' in hand:
                return CardType.FIVE_OF_A_KIND
            return CardType.FOUR_OF_A_KIND
        case [2, 3]:
            if 'J' in hand:
                return CardType.FIVE_OF_A_KIND
            return CardType.FULL_HOUSE
        case [1, 1, 3]:
            if joker and 'J' in hand:
                return CardType.FULL_HOUSE
            return CardType.THREE_OF_A_KIND
        case [1, 2, 2]:
            if joker and counts['J'] == 2:
                return CardType.FOUR_OF_A_KIND
            if joker and counts['J'] == 1:
                return CardType.THREE_OF_A_KIND
            return CardType.TWO_PAIR
        case [1, 1, 1, 2]:
            if joker and 'J' in hand:
                return CardType.THREE_OF_A_KIND
            return CardType.ONE_PAIR
        case _:
            if joker and 'J' in hand:
                return CardType.ONE_PAIR
            return CardType.HIGH_CARD


def compare(hand1: str, hand2: str, joker: bool = False) -> int:
    type_lhs = card_type(hand1)
    type_rhs = card_type(hand2)

    if type_lhs < type_rhs:
        return -1

    if type_lhs > type_rhs:
        return 1

    strength = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'J': 4,
        'T': 5,
        '9': 6,
        '8': 7,
        '7': 8,
        '6': 9,
        '5': 10,
        '4': 11,
        '3': 12,
        '2': 13,
    }

    if joker:
        strength['J'] = 14

    for v1, v2 in zip(hand1, hand2):
        if strength[str(v1)] > strength[str(v2)]:
            return -1
        if strength[str(v1)] < strength[str(v2)]:
            return 1

    raise NotImplementedError(f'Cards are the same: {hand1}, {hand2}.')


def order_by_rank(cards: list[str], joker=False) -> list[str]:

    return sorted(cards, key=functools.cmp_to_key(compare))


def part1(filename: str) -> int:
    hand_to_bid = parse_input(filename)
    sorted_hands = sorted(hand_to_bid, key=functools.cmp_to_key(compare))
    acc = 0
    for pos, hand in enumerate(sorted_hands, start=1):
        acc += hand_to_bid[hand] * pos
    return acc


def part2(filename: str) -> int:
    return 42


def main() -> None:
    # print(f'Part 1, Sample: {part1("aoc_2023/day07/sample.txt")}')  # 6440
    # print(f'Part 1, Input: {part1("aoc_2023/day07/input.txt")}')  # 246_163_188

    print(f'Part 2, Sample: {part2("aoc_2023/day07/sample.txt")}')  # 5905
    # print(f'Part 2, Input: {part2("aoc_2023/day07/input.txt")}')  #


if __name__ == '__main__':
    main()
