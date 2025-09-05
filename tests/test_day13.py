import unittest

from aoc_2023.day13 import main


class TestPart1(unittest.TestCase):

    def test_when_called_then_return_forty_two(self):
        # Arrange
        expected = 42

        # Act
        actual = main.part1('aoc_2023/day13/sample.txt')

        # Assert
        self.assertEqual(actual, expected)
