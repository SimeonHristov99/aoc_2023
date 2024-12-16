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


class TestGetState(unittest.TestCase):
    """
    Class for testing the function that outputs whether a spring arrangement is valid or a full group (i.e. valid and a full group).
    """

    def test_returns_valid_if_not_yet_a_group(self):
        """
        Tests that the function returns "valid" when the substring does not represent a group.
        """
        # Arrange
        substring = '##'
        current_group = 3
        expected = 'valid'

        # Act
        actual = main.get_state(substring, current_group)

        # Assert
        self.assertEqual(actual, expected)

    def test_returns_full_group_if_a_group(self):
        """
        Tests that the function returns "full_group" when the substring represents a group.
        """
        # Arrange
        substring = '###'
        current_group = 3
        expected = 'full_group'

        # Act
        actual = main.get_state(substring, current_group)

        # Assert
        self.assertEqual(actual, expected)


class TestGetNumCombinations(unittest.TestCase):
    """
    Class for testing the function that produces the number possibilities for broken and working springs.
    """

    def test_works_for_first_example(self):
        """
        Tests that the function works for the first example: "???.###".
        """
        # Arrange
        pattern = ['?', '?', '?', '.', '#', '#', '#']
        num_broken = [1, 1, 3]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)
