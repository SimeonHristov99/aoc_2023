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
            ('???.###', [1, 1, 3]),
            ('.??..??...?##.', [1, 1, 3]),
            ('?#?#?#?#?#?#?#?', [1, 3, 1, 6]),
            ('????.#...#...', [4, 1, 1]),
            ('????.######..#####.', [1, 6, 5]),
            ('?###????????', [3, 2, 1]),
        ]

        # Act
        actual = main.parse(file)

        # Assert
        self.assertListEqual(actual, expected)


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

    def test_only_pattern_more_than_one_character_and_group_returns_one(self):
        """
        Tests that when the pattern can be entirely filled in with the current group, the output is 1.
        """
        # Arrange
        pattern = '???'
        num_broken = [3]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_one_possibility_with_question_marks_works(self):
        """
        Tests that when there are multiple question marks and multiple groups, but the possible grouping is only 1, it gets outputted.
        """
        # Arrange
        pattern = '???'
        num_broken = [1, 1]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_first_example(self):
        """
        Tests that the function works for the first example: "???.###".
        """
        # Arrange
        pattern = '???.###'
        num_broken = [1, 1, 3]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_second_example(self):
        """
        Tests that the function works for the second example: ".??..??...?##.".
        """
        # Arrange
        pattern = '.??..??...?##.'
        num_broken = [1, 1, 3]
        expected = 4

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_third_example(self):
        """
        Tests that the function works for the second example: "?#?#?#?#?#?#?#?".
        """
        # Arrange
        pattern = '?#?#?#?#?#?#?#?'
        num_broken = [1, 3, 1, 6]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_fourth_example(self):
        """
        Tests that the function works for the second example: "????.#...#...".
        """
        # Arrange
        pattern = '????.#...#...'
        num_broken = [4, 1, 1]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_fifth_example(self):
        """
        Tests that the function works for the second example: "????.######..#####.".
        """
        # Arrange
        pattern = '????.######..#####.'
        num_broken = [1, 6, 5]
        expected = 4

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_sixth_example(self):
        """
        Tests that the function works for the second example: "?###????????".
        """
        # Arrange
        pattern = '?###????????'
        num_broken = [3, 2, 1]
        expected = 10

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(actual, expected)

    def test_large_example(self):
        """
        Tests that the function works with a large example.
        """
        # Arrange
        pattern = '???.###????.###????.###????.###????.###'
        num_broken = [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3]
        expected = 1

        # Act
        actual = main.get_num_combinations(pattern, num_broken)

        # Assert
        self.assertEqual(expected, actual)


class Part1(unittest.TestCase):
    """
    Class for testing the function that completes part 1.
    """

    def test_works_for_sample(self):
        """
        Tests that the function produces the correct output for the sample.
        """
        # Arrange
        filename = 'aoc_2023/day12/sample.txt'
        expected = 21

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)

    def test_works_for_input(self):
        """
        Tests that the function produces the correct output for the input.
        """
        # Arrange
        filename = 'aoc_2023/day12/input.txt'
        expected = 7110

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)
