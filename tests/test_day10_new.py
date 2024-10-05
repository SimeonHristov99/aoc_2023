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
        ], [['.', '.', '.', '.', '.'],
            ['.', 'S', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'J', '.'],
            ['.', '.', '.', '.', '.']]
        ]
        actuals = []

        # Act
        for input_file in filenames:
            actuals.append(main.parse_input(input_file))

        # Assert
        self.assertListEqual(actuals, expecteds)
