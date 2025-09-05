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

    def test_when_called_then_returns_tuple_with_empty_lists(self):
        # Arrange
        expected = ([], [])
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
        self.assertTupleEqual(actual, expected)


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
