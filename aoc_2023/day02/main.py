from functools import reduce
from attr import field
from aoc_2023 import utils
from attrs import define
from enum import Enum
import sys


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

    cubes: list[Cube]

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

    def parse_cube_sets(cube_drafts: str) -> list[list[Cube]]:
        cube_drafts_res = []
        for cube_set in cube_drafts.split(';'):
            cubes = []
            cube_drafts = cube_set.strip().split(', ')
            for cube_draft in cube_drafts:
                cube_value, cube_color = cube_draft.split()
                cube = Cube(color=Color[cube_color.upper()], amount=cube_value)
                cubes.append(cube)
            cube_drafts_res.append(cubes)
        return cube_drafts_res

    def satisfies(self, configuration) -> bool:
        self_totals = self.count_totals()
        totals_limit = configuration.count_totals()

        print(self.cubes)
        totals = f'{self_totals}'
        print(f'{totals.ljust(15)} {totals_limit}')

        return all(other >= my for my, other in zip(self_totals, totals_limit))


@define
class Game:
    id: int = field(converter=int)
    cube_set: list[CubeSet]

    def is_possible(self, configuration: CubeSet) -> bool:
        return self.cube_set.satisfies(configuration)


def parse(line: str) -> Game:
    game_info, cube_drafts = line.split(':')
    game_info = game_info.split()

    cube_set = CubeSet(cubes=CubeSet.parse_cube_sets(cube_drafts))

    game = Game(
        id=game_info[-1],
        cube_set=cube_set
    )

    return game


def part1(filename: str) -> int:
    config_to_check = '12 red, 13 green, 14 blue'
    lines = utils.get_lines(filename)

    games = [parse(game) for game in lines]
    cs_check = CubeSet(cubes=CubeSet.parse_cube_sets(config_to_check))

    res = 0
    for game in games:
        print(game.id)
        if game.is_possible(cs_check):
            print('Possible.')
            res += game.id
        else:
            print('Impossible.')
        print('\n')

    return res


def part2(filename: str) -> int:
    return 42


def main() -> None:
    print(f'Part 1, Sample: {part1("aoc_2023/day02/sample.txt")}')

    with open('outputs.txt', 'w') as f:
        sys.stdout = f
        print(f'Part 1, Input: {part1("aoc_2023/day02/input.txt")}')
    # 204 => too low

    # print(f'Part 2, Sample: {part2("aoc_2023/day02/sample.txt")}')
    # print(f'Part 2, Input: {part2("aoc_2023/day02/input.txt")}')


if __name__ == '__main__':
    main()
