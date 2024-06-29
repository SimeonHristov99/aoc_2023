import enum


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


def card_type(hand: str) -> CardType:
    if is_five_of_a_kind(hand):
        return CardType.FIVE_OF_A_KIND

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
