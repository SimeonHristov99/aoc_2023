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
        expected = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
        ]

        # Act
        actual = main.Summarizer(expected).pattern

        # Assert
        self.assertListEqual(actual, expected)


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
        summarizer = main.Summarizer(pattern)

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
        summarizer = main.Summarizer(pattern)

        # Act
        actual = summarizer.create_reflection_maps()

        # Assert
        self.assertDictEqual(actual[0], expected[0])
        self.assertDictEqual(actual[1], expected[1])


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
        summarizer = main.Summarizer(pattern)

        # Act
        actual = summarizer.summarize_column(0)

        # Assert
        self.assertEqual(actual, expected)


class TestSummarizerSummarizeRow(unittest.TestCase):

    def test_when_called_then_return_zero(self):
        # Arrange
        expected = 0
        pattern = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#....#..#',
        ]
        summarizer = main.Summarizer(pattern)

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
        summarizer = main.Summarizer(pattern)
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

    def test_when_called_on_columns_then_returns_zero(self):
        # Arrange
        expected = 0
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
        summarizer = main.Summarizer(pattern)
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

    def test_when_called_then_return_zero(self):
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
        summarizer = main.Summarizer(pattern)

        # Act
        actual = summarizer.summarize()

        # Assert
        self.assertEqual(actual, expected)


class TestPart1(unittest.TestCase):

    def test_when_called_on_sample_then_returns_zero(self):
        # Arrange
        expected = 0

        # Act
        actual = main.part1('aoc_2023/day13/sample.txt')

        # Assert
        self.assertEqual(actual, expected)

    def test_when_called_on_input_then_returns_zero(self):
        # Arrange
        expected = 0

        # Act
        actual = main.part1('aoc_2023/day13/input.txt')

        # Assert
        self.assertEqual(actual, expected)
