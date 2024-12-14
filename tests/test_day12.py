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


class TestCountCombinations(unittest.TestCase):
    """
    Class for testing the function that counts the possibilities for broken and working springs.
    """

    def test_base_case_out_of_bounds_index_and_empty_list_with_groups(self):
        """
        Tests that when the current index is out of bounds and the list with groups is empty the output is 1 since that means the group was successfully obtained (we'll always have at least one group).
        """
        # Arrange
        result = ''
        idx_start = 0
        idx_current = 1
        num_broken = []
        pattern = []
        expected = 1

        # Act
        actual = main.create_combinations(num_broken, result, idx_start, idx_current,
                                          iter(num_broken), iter(pattern))

        # Assert
        self.assertEqual(actual, expected)

    def test_base_case_out_of_bounds_index_and_non_empty_list_with_groups(self):
        """
        Tests that when the current index is out of bounds and the list with groups is not empty the output is 0 since that means the last group was not obtained.
        """
        # Arrange
        result = ''
        idx_start = 0
        idx_current = 2
        num_broken = [1]
        pattern = []
        expected = 0

        # Act
        actual = main.create_combinations(num_broken, result, idx_start, idx_current,
                                          iter(num_broken), iter(pattern))

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
