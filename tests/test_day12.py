import unittest

from aoc_2023.day12 import main


class TestParse(unittest.TestCase):
    """
    Class for testing the function that parses the input.
    """

    def test_parse_sample(self):
        """
        Tests that the sample is parsed correctly.
        """
        # Arrange
        file = 'aoc_2023/day12/sample.txt'
        expected = [
            (['?', '?', '?', '.', '#', '#', '#'], [1, 1, 3]),
            (['.', '?', '?', '.', '.', '?', '?', '.', '.', '.', '?', '#', '#', '.'], [1, 1, 3]),
            (['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#',
              '?'], [1, 3, 1, 6]),
            (['?', '?', '?', '?', '.', '#', '.', '.', '.', '#', '.', '.', '.'], [4, 1, 1]),
            ([
                '?', '?', '?', '?', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#',
                '#', '#', '.'
            ], [1, 6, 5]),
            (['?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?'], [3, 2, 1]),
        ]

        # Act
        actual = main.parse(file)

        # Assert
        self.assertListEqual(actual, expected)
