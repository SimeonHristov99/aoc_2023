from __future__ import annotations

from enum import Enum
from functools import reduce

from attrs import define, field

from aoc_2023 import utils


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


@define
class Cube:
    color: Color
    amount: int = field(converter=int)


@define
class CubeSet:
    total_reds: int = field(default=0, init=False)
    total_greens: int = field(default=0, init=False)
    total_blues: int = field(default=0, init=False)

    cubes: list[list[Cube]]

    def count_totals(self) -> tuple[int, int, int]:
        amount_greens = 0
        amount_reds = 0
        amount_blues = 0

        for cube_draft in self.cubes:
            for cube in cube_draft:
                match cube.color:
                    case Color.RED:
                        amount_reds += cube.amount
                    case Color.GREEN:
                        amount_greens += cube.amount
                    case Color.BLUE:
                        amount_blues += cube.amount

        return (amount_reds, amount_greens, amount_blues)

    @staticmethod
    def parse_cube_sets(cube_drafts: str) -> list[list[Cube]]:
        cube_drafts_res = []
        for cube_set in cube_drafts.split(';'):
            cubes = []
            cube_drafts_splits = cube_set.strip().split(', ')
            for cube_draft in cube_drafts_splits:
                cube_value, cube_color = cube_draft.split()
                cube = Cube(Color[cube_color.upper()], cube_value)
                cubes.append(cube)
            cube_drafts_res.append(cubes)
        return cube_drafts_res

    def satisfies(self, configuration) -> bool:
        limit_reds, limit_greens, limit_blues = configuration.count_totals()
        for cube_draft in self.cubes:
            for cube in cube_draft:
                match cube.color:
                    case Color.RED:
                        if cube.amount > limit_reds:
                            return False
                    case Color.GREEN:
                        if cube.amount > limit_greens:
                            return False
                    case Color.BLUE:
                        if cube.amount > limit_blues:
                            return False
        return True

    def min_cube_set(self) -> int:
        reds = []
        blues = []
        greens = []

        for cube_draft in self.cubes:
            for cube in cube_draft:
                match cube.color:
                    case Color.RED:
                        reds.append(cube.amount)
                    case Color.GREEN:
                        greens.append(cube.amount)
                    case Color.BLUE:
                        blues.append(cube.amount)

        min_reds = max(reds)
        min_blues = max(blues)
        min_greens = max(greens)

        return min_reds * min_blues * min_greens


@define
class Game:
    id: int = field(converter=int)
    cube_set: CubeSet

    def is_possible(self, configuration: CubeSet) -> bool:
        return self.cube_set.satisfies(configuration)

    def minimum_cube_set_power(self) -> int:
        return self.cube_set.min_cube_set()


def parse(line: str) -> Game:
    game_infos, cube_drafts = line.split(':')
    game_info = game_infos.split()

    cube_set = CubeSet(CubeSet.parse_cube_sets(cube_drafts))

    game = Game(game_info[-1], cube_set)

    return game


def part1(filename: str) -> int:
    config_to_check = '12 red, 13 green, 14 blue'
    lines = utils.get_lines(filename)
    games = [parse(game) for game in lines]
    cs_check = CubeSet(CubeSet.parse_cube_sets(config_to_check))

    res = 0
    for game in games:
        if game.is_possible(cs_check):
            res += game.id
    return res


def part2(filename: str) -> int:
    lines = utils.get_lines(filename)
    games = [parse(game) for game in lines]
    return reduce(
        lambda acc, game: acc + game.minimum_cube_set_power(),
        games,
        0,
    )


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day02/sample.txt")}')
    print(f'Part 1, Input: {part1("aoc_2023/day02/input.txt")}')

    print(f'Part 2, Sample: {part2("aoc_2023/day02/sample.txt")}')
    print(f'Part 2, Input: {part2("aoc_2023/day02/input.txt")}')


if __name__ == '__main__':
    main()
