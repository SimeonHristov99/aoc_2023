import unittest

import pytest

from aoc_2023.day10_new import main


class TestDay10New(unittest.TestCase):

    def test_parse_input(self):
        """
        Tests that the input is parsed correctly.
        """
        # Arrange
        filenames = ['aoc_2023/day10/sample1.txt', 'tests/resources/d10_s1.txt']
        expecteds = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                     [['.', '.', '.', '.', '.'], ['.', 'S', '-', '7', '.'],
                      ['.', '|', '.', '|', '.'], ['.', 'L', '-', 'J', '.'],
                      ['.', '.', '.', '.', '.']]]
        actuals = []

        # Act
        for input_file in filenames:
            actuals.append(main.parse_input(input_file))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_find_start(self):
        """
        Tests that the symbol, marking the starting pipe - S, is found correctly.
        """
        # Arrange
        inputs = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                  [['.', '.', 'F', '7', '.'], ['.', 'F', 'J', '|', '.'], ['S', 'J', '.', 'L', '7'],
                   ['|', 'F', '-', '-', 'J'], ['L', 'J', '.', '.', '.']]]
        expecteds = [(1, 1), (2, 0)]
        actuals = []

        # Act
        for input_map in inputs:
            actuals.append(main.find_start(input_map))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_get_loop_coordinates(self):
        """
        Tests the loop coordinates are obtained successfully.
        """
        # Arrange
        inputs = [
            main.parse_input('tests/resources/d10_s1.txt'),
            main.parse_input('tests/resources/d10_s2.txt'),
            # main.parse_input('tests/resources/d10_s3.txt'),
            # main.parse_input('aoc_2023/day10_new/sample.txt'),
            # main.parse_input('aoc_2023/day10_new/input.txt'),
        ]
        expecteds = [
            [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)],
            [
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8),
                (4, 8), (5, 8), (6, 8), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6),
                (5, 7), (4, 7), (3, 7), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2),
                (4, 2), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1),
                (5, 1), (4, 1), (3, 1), (2, 1)
            ],
        ]
        actuals = []

        # Act
        for input_map in inputs:
            start = main.find_start(input_map)
            actuals.append(main.get_loop_coordinates(input_map, start))

        # Assert
        self.assertListEqual(actuals, expecteds)
