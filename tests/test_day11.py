import unittest

from aoc_2023.day11 import main


class TestParse(unittest.TestCase):
    """
    Class for testing the function that parses the input.
    """

    def test_parse_sample(self):
        """
        Tests that the sample is parsed correctly.
        """
        # Arrange
        file = 'aoc_2023/day11/sample.txt'
        expected = [
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ]

        # Act
        actual = main.parse(file)

        # Assert
        self.assertListEqual(actual, expected)
