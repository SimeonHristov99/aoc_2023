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


class TestIsWorkingCombination(unittest.TestCase):
    """
    Class for testing the function that outputs whether a spring arrangement is compatible with a list of given groups.
    """

    def test_returns_false_if_not_compatible(self):
        """
        Tests that the function returns False when the substring is not compatible.
        """
        # Arrange
        substring = '##'
        groups = [3]

        # Act
        actual = main.is_working_combination(substring, groups)

        # Assert
        self.assertFalse(actual)

    def test_returns_true_if_a_group(self):
        """
        Tests that the function returns "True" when the substring is compatible.
        """
        # Arrange
        substring = '###'
        groups = [3]

        # Act
        actual = main.is_working_combination(substring, groups)

        # Assert
        self.assertTrue(actual)

    def test_returns_true_on_multiple_versions(self):
        """
        Tests that the function returns "True" when the substring is compatible - multiple versions with the same group.
        """
        # Arrange
        substrings = [
            '.###.##.#...',
            '.###.##..#..',
            '.###.##...#.',
            '.###.##....#',
            '.###..##.#..',
            '.###..##..#.',
            '.###..##...#',
            '.###...##.#.',
            '.###...##..#',
            '.###....##.#',
        ]
        groups = [3, 2, 1]
        expecteds = [True] * len(substrings)

        # Act
        actuals = [main.is_working_combination(substring, groups) for substring in substrings]

        # Assert
        self.assertListEqual(actuals, expecteds)


class TestGetNumCombinations(unittest.TestCase):
    """
    Class for testing the function that produces the number possibilities for broken and working springs.
    """

    def test_only_pattern_exactly_one_character_and_group_returns_one(self):
        """
        Tests that when the pattern is one character and the current group is 1, the output is 1.
        """
        # Arrange
        pattern = '?'
        num_broken = [1]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_one_unknown_and_one_given(self):
        """
        Tests that when there is one unknown status and one given, the result is 1.
        """
        # Arrange
        patterns = ['?#', '#?']
        num_broken = [1]
        expecteds = [1, 1]

        # Act
        actuals = [main.get_num_combinations(pattern, num_broken) for pattern in patterns]

        # Assert
        self.assertEqual(actuals, expecteds)


#     def test_only_pattern_more_than_one_character_and_group_returns_one(self):
#         """
#         Tests that when the pattern can be entirely filled in with the current group, the output is 1.
#         """
#         # Arrange
#         pattern = ['?', '?', '?']
#         num_broken = [3]
#         expected = 1

#         # Act
#         actual = main.get_num_combinations(pattern, num_broken)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_one_possibility_with_question_marks_works(self):
#         """
#         Tests that when there are multiple question marks and multiple groups, but the possible grouping is only 1, it gets outputted.
#         """
#         # Arrange
#         pattern = ['?', '?', '?']
#         num_broken = [1, 1]
#         expected = 1

#         # Act
#         actual = main.get_num_combinations(pattern, num_broken)

#         # Assert
#         self.assertEqual(actual, expected)

#     def test_works_for_first_example(self):
#         """
#         Tests that the function works for the first example: "???.###".
#         """
#         # Arrange
#         pattern = ['?', '?', '?', '.', '#', '#', '#']
#         num_broken = [1, 1, 3]
#         expected = 1

#         # Act
#         actual = main.get_num_combinations(pattern, num_broken)

#         # Assert
#         self.assertEqual(actual, expected)
