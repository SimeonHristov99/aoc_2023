import os
import unittest

from aoc_2023.day13 import main


class TestParseInput(unittest.TestCase):

    def test_when_two_patterns_passed_then_returns_two_lists_each_with_one_pattern(self):
        # Arrange
        filename = os.path.join('aoc_2023', 'day13', 'sample.txt')
        expected = [[
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ],
                    [
                        '#...##..#',
                        '#....#..#',
                        '..##..###',
                        '#####.##.',
                        '#####.##.',
                        '..##..###',
                        '#....#..#',
                    ]]

        # Act
        actual = main.parse_input(filename)

        # Assert
        self.assertListEqual(actual, expected, f'\n{actual=}\n{expected=}\n')


class TestPart1(unittest.TestCase):

    def test_when_called_then_return_forty_two(self):
        # Arrange
        expected = 42

        # Act
        actual = main.part1('aoc_2023/day13/sample.txt')

        # Assert
        self.assertEqual(actual, expected)
