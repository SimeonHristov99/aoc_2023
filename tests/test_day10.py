import unittest

import pytest

from aoc_2023.day10 import main


class TestDay10(unittest.TestCase):

    def test_find_one(self):
        """
        Tests that the coordinates of the starting point are correctly found.
        """
        # Arrange
        matrices = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                    [
                        ['7', '-', 'F', '7', '-'],
                        ['.', 'F', 'J', '|', '7'],
                        ['S', 'J', 'L', 'L', '7'],
                        ['|', 'F', '-', '-', 'J'],
                        ['L', 'J', '.', 'L', 'J'],
                    ]]
        expectations = [(1, 1), (2, 0)]
        actuals = []

        # Act
        for matrix in matrices:
            actuals.append(main.find_one(matrix))

        # Assert
        self.assertListEqual(actuals, expectations)

    def test_find_one_raises_when_no_one(self):
        """
        Tests that an exception is raised when 'S' is not found.
        """
        # Arrange
        matrix = [['-', 'L', '|', 'F', '7'], ['7', 'G', '-', '7', '|']]
        expected_text = 'Coordinates of starting point not found.'

        # Act
        with pytest.raises(NotImplementedError) as exception_context:
            _ = main.find_one(matrix)
        actual_text = str(exception_context.value)

        # Assert
        self.assertEqual(actual_text, expected_text)
