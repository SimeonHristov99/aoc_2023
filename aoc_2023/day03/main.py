from __future__ import annotations

import math

from aoc_2023 import utils


def extract_number(
    schematic: list[str],
    visited: set[tuple[int, int]],
    coords: tuple[int, int],
) -> int:

    def helper(direction: int) -> str:
        i = coords[0]
        j = coords[1] if direction == -1 else coords[1] + 1
        number_part = ''
        while (utils.valid_coords(i, j, schematic) and schematic[i][j].isnumeric()):
            number_part += schematic[i][j]
            visited.add((i, j))
            j += direction

        if direction == -1:
            return ''.join(reversed(number_part))
        return number_part

    part1 = helper(-1)
    part2 = helper(1)
    result = int(part1 + part2)
    return result


def part1(filename: str) -> int:
    schematic = utils.get_lines(filename)

    n_rows = len(schematic)
    n_cols = len(schematic[0])

    visited: set[tuple[int, int]] = set()
    numbers = []

    for i in range(n_rows):
        for j in range(n_cols):
            if not schematic[i][j].isnumeric() and schematic[i][j] != '.':
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        coords = (i + ii, j + jj)
                        if (utils.valid_coords(i + ii, j + jj, schematic)
                                and schematic[i + ii][j + jj].isnumeric()
                                and coords not in visited):
                            number = extract_number(schematic, visited, coords)
                            numbers.append(number)

    return sum(numbers)


def part2(filename: str) -> int:
    schematic = utils.get_lines(filename)

    n_rows = len(schematic)
    n_cols = len(schematic[0])

    visited: set[tuple[int, int]] = set()
    result = 0

    for i in range(n_rows):
        for j in range(n_cols):
            if schematic[i][j] == '*':
                numbers = []
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        coords = (i + ii, j + jj)
                        if (utils.valid_coords(i + ii, j + jj, schematic)
                                and schematic[i + ii][j + jj].isnumeric()
                                and coords not in visited):
                            number = extract_number(schematic, visited, coords)
                            numbers.append(number)
                if len(numbers) == 2:
                    result += math.prod(numbers)

    return result


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day03/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day03/input.txt")}')

    print(f'Part 2, Sample: {part2("aoc_2023/day03/sample.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day03/input.txt")}')


if __name__ == '__main__':
    main()
