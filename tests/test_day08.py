import unittest

from aoc_2023.day08 import main


class TestDay08(unittest.TestCase):

    def test_parsing_input(self):
        """
        Tests that parsing the input returns a tuple with the directions and a dictionary from node to children.
        """
        # Arrange
        filename = 'aoc_2023/day08/sample2.txt'
        expected_directions = 'LLR'
        expected_map = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }

        # Act
        actual_directions, actual_map = main.parse_input(filename)

        # Assert
        self.assertEqual(actual_directions, expected_directions)
        self.assertEqual(actual_map, expected_map)

    def test_get_num_steps_v1(self):
        """
        Tests that obtaining the number of steps works - variant 1.
        """
        # Arrange
        directions = 'LLR'
        map_ = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }
        expected = 6

        # Act
        actual = main.num_steps(directions, map_)

        # Assert
        self.assertEqual(expected, actual)

    def test_get_num_steps_v2(self):
        """
        Tests that obtaining the number of steps works - variant 2.
        """
        # Arrange
        directions = 'RL'
        map_ = {
            'AAA': ('BBB', 'CCC'),
            'BBB': ('DDD', 'EEE'),
            'CCC': ('ZZZ', 'GGG'),
            'DDD': ('DDD', 'DDD'),
            'EEE': ('EEE', 'EEE'),
            'GGG': ('GGG', 'GGG'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }
        expected = 2

        # Act
        actual = main.num_steps(directions, map_)

        # Assert
        self.assertEqual(expected, actual)
