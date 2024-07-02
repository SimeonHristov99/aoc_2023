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
