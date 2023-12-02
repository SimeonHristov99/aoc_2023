import sys
from functools import reduce
from aoc_2023.utils import get_lines

DIGIT_LETTERS_MAP = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def part1(filename: str) -> int:
    lines = get_lines(filename)

    numbers = []

    for line in lines:
        digit1 = None
        digit2 = None

        for character in line:
            if character.isdigit():
                digit1 = character
                break

        for character in line[::-1]:
            if character.isdigit():
                digit2 = character
                break

        numbers.append(int(digit1 + digit2))

    return sum(numbers)

def parse(line: str) -> int:
    digits = []

    i = 0
    while i < len(line):
        if line[i].isdigit():
            digits.append(int(line[i]))
        else:
            for letter in DIGIT_LETTERS_MAP:
                if line[i:].startswith(letter):
                    digits.append(DIGIT_LETTERS_MAP.get(letter))
                    break

        i += 1

    return int(f'{digits[0]}{digits[-1]}')

def part2(filename: str) -> int:
    lines = get_lines(filename)
    result = reduce(lambda acc, line: acc + parse(line), lines, 0)
    return result


def main() -> None:
    print(f'Part 1, Sample 1: {part1("aoc_2023/day01/sample1.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day01/input.txt")}')

    print(f'Part 2, Sample 2: {part2("aoc_2023/day01/sample2.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day01/input.txt")}')


if __name__ == '__main__':
    main()
