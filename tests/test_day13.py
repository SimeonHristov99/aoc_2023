import os
import unittest

from aoc_2023.day13 import main


class TestParseInput(unittest.TestCase):

    def test_when_two_patterns_passed_then_returns_two_lists_each_with_one_pattern(self):
        # Arrange
        filename = os.path.join('aoc_2023', 'day13', 'sample.txt')
        expected = [[
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ],
                    [
                        '#...##..#',
                        '#....#..#',
                        '..##..###',
                        '#####.##.',
                        '#####.##.',
                        '..##..###',
                        '#....#..#',
                    ]]

        # Act
        actual = main.parse_input(filename)

        # Assert
        self.assertListEqual(actual, expected, f'\n{actual=}\n{expected=}\n')


class TestSummarizerInit(unittest.TestCase):

    def test_when_created_then_user_can_pass_pattern(self):
        # Arrange
        expected_pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        expected_smudge = False

        # Act
        summarizer = main.Summarizer(expected_pattern, expected_smudge)
        actual_pattern = summarizer.pattern
        actual_smudge = summarizer.with_smudge

        # Assert
        self.assertListEqual(actual_pattern, expected_pattern)
        self.assertEqual(actual_smudge, expected_smudge)


class TestSummarizerCreateReflectionMaps(unittest.TestCase):

    def test_when_equal_rows_and_columns_then_returns_equal_rows_and_cols_indices(self):
        # Arrange
        expected = ({
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6)],
            4: [(4, 5), (3, 6)],
            5: [(5, 6)]
        }, {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6), (0, 7)],
            4: [(4, 5), (3, 6), (2, 7), (1, 8)],
            5: [(5, 6), (4, 7), (3, 8)],
            6: [(6, 7), (5, 8)],
            7: [(7, 8)]
        })
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)

        # Act
        actual = summarizer.create_reflection_maps()

        # Assert
        self.assertDictEqual(actual[0], expected[0])
        self.assertDictEqual(actual[1], expected[1])

    def test_when_nonequal_rows_and_columns_then_returns_nonequal_rows_and_cols_indices(self):
        # Arrange
        expected = ({
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3)],
        }, {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6), (0, 7)],
            4: [(4, 5), (3, 6), (2, 7), (1, 8)],
            5: [(5, 6), (4, 7), (3, 8)],
            6: [(6, 7), (5, 8)],
            7: [(7, 8)]
        })
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)

        # Act
        actual = summarizer.create_reflection_maps()

        # Assert
        self.assertDictEqual(actual[0], expected[0])
        self.assertDictEqual(actual[1], expected[1])


class TestSummarizerFormsReflection(unittest.TestCase):

    def test_when_columns_not_reflecting_without_smudge_then_returns_false(self):
        # Arrange
        expected = False
        with_smudge = False
        direction = main.Direction.COLS
        columns_to_check = [(1, 2), (0, 3)]
        pattern = [
            '#...#',
            '....#',
            '#..#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(columns_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_columns_reflecting_without_smudge_then_returns_true(self):
        # Arrange
        expected = True
        with_smudge = False
        direction = main.Direction.COLS
        columns_to_check = [(4, 5), (3, 6), (2, 7), (1, 8)]
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(columns_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_columns_not_reflecting_with_smudge_then_returns_false(self):
        # Arrange
        expected = False
        with_smudge = True
        direction = main.Direction.COLS
        columns_to_check = [(1, 2), (0, 3)]
        pattern = [
            '#...#',
            '...##',
            '#..#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(columns_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_columns_reflecting_with_smudge_then_returns_true(self):
        # Arrange
        expected = True
        with_smudge = True
        direction = main.Direction.COLS
        columns_to_check = [(1, 2), (0, 3)]
        pattern = [
            '#...#',
            '....#',
            '#..#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(columns_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_rows_not_reflecting_without_smudge_then_returns_false(self):
        # Arrange
        expected = False
        with_smudge = False
        direction = main.Direction.ROWS
        rows_to_check = [(0, 1)]
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(rows_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_rows_reflecting_without_smudge_then_returns_true(self):
        # Arrange
        expected = True
        with_smudge = False
        direction = main.Direction.ROWS
        rows_to_check = [(3, 4), (2, 5), (1, 6)]
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(rows_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_rows_not_reflecting_with_smudge_then_returns_false(self):
        # Arrange
        expected = False
        with_smudge = True
        direction = main.Direction.ROWS
        rows_to_check = [(4, 5), (3, 6)]
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(rows_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_rows_reflecting_with_smudge_then_returns_true(self):
        # Arrange
        expected = True
        with_smudge = True
        direction = main.Direction.ROWS
        rows_to_check = [(0, 1)]
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge)

        # Act
        actual = summarizer.forms_reflection(rows_to_check, direction)

        # Assert
        self.assertEqual(actual, expected)


class TestSummarizerSummarizeColumn(unittest.TestCase):

    def test_when_line_is_not_reflection_then_return_zero(self):
        # Arrange
        expected = 0
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_vertical = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6), (0, 7)],
            4: [(4, 5), (3, 6), (2, 7), (1, 8)],
            5: [(5, 6), (4, 7), (3, 8)],
            6: [(6, 7), (5, 8)],
            7: [(7, 8)]
        }

        # Act
        actual = summarizer.summarize_column(0)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_line_is_reflection_then_return_summary(self):
        # Arrange
        expected = 5
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_vertical = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6), (0, 7)],
            4: [(4, 5), (3, 6), (2, 7), (1, 8)],
            5: [(5, 6), (4, 7), (3, 8)],
            6: [(6, 7), (5, 8)],
            7: [(7, 8)]
        }

        # Act
        actual = summarizer.summarize_column(4)

        # Assert
        self.assertEqual(actual, expected)


class TestSummarizerSummarizeRow(unittest.TestCase):

    def test_when_line_is_not_reflection_then_return_zero(self):
        # Arrange
        expected = 0
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_horizontal = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6)],
            4: [(4, 5), (3, 6)],
            5: [(5, 6)]
        }

        # Act
        actual = summarizer.summarize_row(0)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_line_is_reflection_then_return_summary(self):
        # Arrange
        expected = 400
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_horizontal = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6)],
            4: [(4, 5), (3, 6)],
            5: [(5, 6)]
        }

        # Act
        actual = summarizer.summarize_row(3)

        # Assert
        self.assertEqual(actual, expected)


class TestSummarizerSummarizeDirection(unittest.TestCase):

    def test_when_called_on_rows_then_returns_zero(self):
        # Arrange
        expected = 0
        direction = main.Direction.ROWS
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_horizontal = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6)],
            4: [(4, 5), (3, 6)],
            5: [(5, 6)]
        }

        # Act
        actual = summarizer.summarize_direction(direction)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_called_on_columns_then_returns_summary(self):
        # Arrange
        expected = 5
        direction = main.Direction.COLS
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)
        summarizer.lines_vertical = {
            0: [(0, 1)],
            1: [(1, 2), (0, 3)],
            2: [(2, 3), (1, 4), (0, 5)],
            3: [(3, 4), (2, 5), (1, 6), (0, 7)],
            4: [(4, 5), (3, 6), (2, 7), (1, 8)],
            5: [(5, 6), (4, 7), (3, 8)],
            6: [(6, 7), (5, 8)],
            7: [(7, 8)]
        }

        # Act
        actual = summarizer.summarize_direction(direction)

        # Assert
        self.assertEqual(actual, expected)


class TestSummarizerSummarize(unittest.TestCase):

    def test_when_called_then_returns_rows_summary(self):
        # Arrange
        expected = 5
        pattern = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]
        summarizer = main.Summarizer(pattern, with_smudge=False)

        # Act
        actual = summarizer.summarize()

        # Assert
        self.assertEqual(actual, expected)


class TestProcess(unittest.TestCase):

    def test_when_without_smudge_on_sample_then_returns_rows_and_columns_summary(self):
        # Arrange
        expected = 405
        with_smudge = False

        # Act
        actual = main.process('aoc_2023/day13/sample.txt', with_smudge)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_without_smudge_on_input_then_returns_rows_and_columns_summary(self):
        # Arrange
        expected = 27742
        with_smudge = False

        # Act
        actual = main.process('aoc_2023/day13/input.txt', with_smudge)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_with_smudge_on_sample_then_returns_rows_and_columns_summary(self):
        # Arrange
        expected = 400
        with_smudge = True

        # Act
        actual = main.process('aoc_2023/day13/sample.txt', with_smudge)

        # Assert
        self.assertEqual(actual, expected)

    def test_when_with_smudge_on_input_then_returns_rows_and_columns_summary(self):
        # Arrange
        expected = 32728
        with_smudge = True

        # Act
        actual = main.process('aoc_2023/day13/input.txt', with_smudge)

        # Assert
        self.assertEqual(actual, expected)
