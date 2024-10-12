import ast
import unittest

from aoc_2023.day10 import main


class TestDay10(unittest.TestCase):

    def test_parse_input(self):
        """
        Tests that the input is parsed correctly.
        """
        # Arrange
        filenames = ['tests/resources/d10_s4.txt', 'tests/resources/d10_s1.txt']
        expecteds = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                     [['.', '.', '.', '.', '.'], ['.', 'S', '-', '7', '.'],
                      ['.', '|', '.', '|', '.'], ['.', 'L', '-', 'J', '.'],
                      ['.', '.', '.', '.', '.']]]
        actuals = []

        # Act
        for input_file in filenames:
            actuals.append(main.parse_input(input_file))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_find_start(self):
        """
        Tests that the symbol, marking the starting pipe - S, is found correctly.
        """
        # Arrange
        inputs = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                  [['.', '.', 'F', '7', '.'], ['.', 'F', 'J', '|', '.'], ['S', 'J', '.', 'L', '7'],
                   ['|', 'F', '-', '-', 'J'], ['L', 'J', '.', '.', '.']]]
        expecteds = [(1, 1), (2, 0)]
        actuals = []

        # Act
        for input_map in inputs:
            actuals.append(main.find_start(input_map))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_get_loop_coordinates_simple_cases(self):
        """
        Tests the loop coordinates are obtained successfully for simple pipe maps.
        """
        # Arrange
        inputs = [
            main.parse_input('tests/resources/d10_s1.txt'),
            main.parse_input('tests/resources/d10_s2.txt'),
            main.parse_input('tests/resources/d10_s3.txt'),
            main.parse_input('aoc_2023/day10/sample.txt')
        ]
        expecteds = [
            [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)],
            [
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8),
                (4, 8), (5, 8), (6, 8), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 6),
                (5, 7), (4, 7), (3, 7), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 2),
                (4, 2), (5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1),
                (5, 1), (4, 1), (3, 1), (2, 1)
            ],
            [
                (0, 4), (0, 3), (1, 3), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3),
                (3, 3), (3, 2), (3, 1), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4),
                (3, 5), (3, 6), (3, 7), (4, 7), (4, 6), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3),
                (6, 2), (7, 2), (7, 3), (7, 4), (6, 4), (6, 5), (7, 5), (7, 6), (8, 6), (8, 5),
                (9, 5), (9, 6), (9, 7), (8, 7), (7, 7), (6, 7), (6, 6), (5, 6), (5, 7), (5, 8),
                (5, 9), (5, 10), (6, 10), (6, 9), (6, 8), (7, 8), (8, 8), (9, 8), (9, 9), (8, 9),
                (7, 9), (7, 10), (8, 10), (9, 10), (9, 11), (8, 11), (7, 11), (6, 11), (6, 12),
                (7, 12), (7, 13), (8, 13), (8, 12), (9, 12), (9, 13), (9, 14), (9, 15), (8, 15),
                (8, 14), (7, 14), (7, 15), (7, 16), (8, 16), (9, 16), (9, 17), (8, 17), (7, 17),
                (7, 18), (8, 18), (8, 19), (7, 19), (6, 19), (6, 18), (6, 17), (6, 16), (6, 15),
                (5, 15), (5, 14), (4, 14), (4, 15), (3, 15), (3, 16), (4, 16), (4, 17), (3, 17),
                (3, 18), (2, 18), (2, 17), (2, 16), (1, 16), (1, 17), (1, 18), (1, 19), (0, 19),
                (0, 18), (0, 17), (0, 16), (0, 15), (1, 15), (2, 15), (2, 14), (1, 14), (0, 14),
                (0, 13), (1, 13), (2, 13), (3, 13), (3, 12), (2, 12), (1, 12), (0, 12), (0, 11),
                (1, 11), (2, 11), (3, 11), (3, 10), (2, 10), (1, 10), (0, 10), (0, 9), (1, 9),
                (2, 9), (3, 9), (4, 9), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8), (0, 7), (1, 7),
                (2, 7), (2, 6), (1, 6), (0, 6), (0, 5), (1, 5), (2, 5), (2, 4), (1, 4)
            ],
            [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4),
             (3, 3), (3, 2), (3, 1), (4, 1), (4, 0), (3, 0)],
        ]
        actuals = []

        # Act
        for input_map in inputs:
            start = main.find_start(input_map)
            actuals.append(main.get_loop_coordinates(input_map, start))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_get_loop_coordinates_input(self):
        """
        Tests the loop coordinates are obtained successfully for the input pipe map.
        """
        # Arrange
        expected = None

        with open('tests/resources/d10_input_loop_coords.txt', 'r') as f:
            expected = ast.literal_eval(f.read())

        input_map = main.parse_input('aoc_2023/day10/input.txt')
        start = main.find_start(input_map)

        # Act
        actual = main.get_loop_coordinates(input_map, start)

        # Assert
        self.assertListEqual(actual, expected)

    def test_part1(self):
        """
        Tests that part 1 returns correct calculations.
        """
        # Arrange
        inputs = [
            './aoc_2023/day10/sample.txt', './aoc_2023/day10/input.txt',
            'tests/resources/d10_s3.txt'
        ]
        expecteds = [8, 6828, 80]
        actuals = []

        # Act
        for filename in inputs:
            actuals.append(main.part1(filename))

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_part2(self):
        """
        Tests that part 2 returns correct calculations.
        """
        # Arrange
        inputs = [
            'tests/resources/d10_s1.txt',
            # 'tests/resources/d10_s2.txt',
            # 'tests/resources/d10_s3.txt',
            # 'tests/resources/d10_s4.txt',
            # './aoc_2023/day10/sample.txt',
            # './aoc_2023/day10/input.txt',
        ]
        expecteds = [1]
        # expecteds = [1, 4, 10, 1, ]
        actuals = []

        # Act
        for filename in inputs:
            actuals.append(main.part2(filename))

        # Assert
        self.assertListEqual(actuals, expecteds)
