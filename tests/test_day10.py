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

    def test_find_start_no_start(self):
        """
        Tests that when the symbol, marking the starting pipe - S, is not found, (-1, -1) is returned.
        """
        # Arrange
        input_map = [['-', 'L', '|', 'F', '7'], ['7', 'L', '-', '7',
                                                 '|'], ['L', '|', '7', '|', '|'],
                     ['-', 'L', '-', 'J', '|'], ['L', '|', '-', 'J', 'F']]
        expected = (-1, -1)

        # Act
        actual = main.find_start(input_map)

        # Assert
        self.assertTupleEqual(actual, expected)

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

    def test_loop_coords_with_difference_only_edges(self):
        """
        Tests that a third dimension is added to the coordinates that
        contains the difference in "x" and "y".
        """
        # Arrange
        inputs = [
            main.parse_input('tests/resources/d10_s1.txt'),
            main.parse_input('tests/resources/d10_s2.txt'),
            main.parse_input('tests/resources/d10_s2_corner_up_right.txt'),
        ]
        loops = []
        for input_map in inputs:
            start = main.find_start(input_map)
            loops.append(main.get_loop_coordinates(input_map, start))

        expecteds = [
            [((1, 1), (1, 2), (0, 1)), ((1, 2), (1, 3), (0, 1)), ((1, 3), (2, 3), (1, 0)),
             ((2, 3), (3, 3), (1, 0)), ((3, 3), (3, 2), (0, -1)), ((3, 2), (3, 1), (0, -1)),
             ((3, 1), (2, 1), (-1, 0)), ((2, 1), (1, 1), (-1, 0))],
            [((1, 1), (1, 2), (0, 1)), ((1, 2), (1, 3), (0, 1)), ((1, 3), (1, 4), (0, 1)),
             ((1, 4), (1, 5), (0, 1)), ((1, 5), (1, 6), (0, 1)), ((1, 6), (1, 7), (0, 1)),
             ((1, 7), (1, 8), (0, 1)), ((1, 8), (2, 8), (1, 0)), ((2, 8), (3, 8), (1, 0)),
             ((3, 8), (4, 8), (1, 0)), ((4, 8), (5, 8), (1, 0)), ((5, 8), (6, 8), (1, 0)),
             ((6, 8), (7, 8), (1, 0)), ((7, 8), (7, 7), (0, -1)), ((7, 7), (7, 6), (0, -1)),
             ((7, 6), (7, 5), (0, -1)), ((7, 5), (6, 5), (-1, 0)), ((6, 5), (5, 5), (-1, 0)),
             ((5, 5), (5, 6), (0, 1)), ((5, 6), (5, 7), (0, 1)), ((5, 7), (4, 7), (-1, 0)),
             ((4, 7), (3, 7), (-1, 0)), ((3, 7), (2, 7), (-1, 0)), ((2, 7), (2, 6), (0, -1)),
             ((2, 6), (2, 5), (0, -1)), ((2, 5), (2, 4), (0, -1)), ((2, 4), (2, 3), (0, -1)),
             ((2, 3), (2, 2), (0, -1)), ((2, 2), (3, 2), (1, 0)), ((3, 2), (4, 2), (1, 0)),
             ((4, 2), (5, 2), (1, 0)), ((5, 2), (5, 3), (0, 1)), ((5, 3), (5, 4), (0, 1)),
             ((5, 4), (6, 4), (1, 0)), ((6, 4), (7, 4), (1, 0)), ((7, 4), (7, 3), (0, -1)),
             ((7, 3), (7, 2), (0, -1)), ((7, 2), (7, 1), (0, -1)), ((7, 1), (6, 1), (-1, 0)),
             ((6, 1), (5, 1), (-1, 0)), ((5, 1), (4, 1), (-1, 0)), ((4, 1), (3, 1), (-1, 0)),
             ((3, 1), (2, 1), (-1, 0)), ((2, 1), (1, 1), (-1, 0))],
            [((4, 6), (4, 7), (0, 1)), ((4, 7), (3, 7), (-1, 0)), ((3, 7), (2, 7), (-1, 0)),
             ((2, 7), (1, 7), (-1, 0)), ((1, 7), (1, 6), (0, -1)), ((1, 6), (1, 5), (0, -1)),
             ((1, 5), (1, 4), (0, -1)), ((1, 4), (1, 3), (0, -1)), ((1, 3), (1, 2), (0, -1)),
             ((1, 2), (2, 2), (1, 0)), ((2, 2), (3, 2), (1, 0)), ((3, 2), (4, 2), (1, 0)),
             ((4, 2), (5, 2), (1, 0)), ((5, 2), (6, 2), (1, 0)), ((6, 2), (6, 3), (0, 1)),
             ((6, 3), (6, 4), (0, 1)), ((6, 4), (6, 5), (0, 1)), ((6, 5), (5, 5), (-1, 0)),
             ((5, 5), (4, 5), (-1, 0)), ((4, 5), (4, 6), (0, 1))],
        ]

        # Act
        actuals = [main.to_differences(loop_coords) for loop_coords in loops]

        # Assert
        self.assertListEqual(actuals, expecteds)

    def test_loop_coords_with_difference_only_edges_corner_up_right(self):
        """
        Tests that coordinates of an upper-right corner get added successfully when looking to the left.
        """
        # Arrange
        side = 'left'
        input_map = main.parse_input('tests/resources/d10_s2_corner_up_right.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4),
                    (5, 3), (5, 4)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_right_up(self):
        """
        Tests that coordinates of an bottom-right corner get added successfully when looking to the right.
        """
        # Arrange
        side = 'right'
        input_map = main.parse_input('tests/resources/d10_s2_corner_right_up.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 5), (2, 6), (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4),
                    (5, 5), (5, 6)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_left_up(self):
        """
        Tests that coordinates of an bottom-left corner get added successfully when looking to the left.
        """
        # Arrange
        side = 'left'
        input_map = main.parse_input('tests/resources/d10_s2_corner_left_up.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 3), (2, 4), (3, 3), (3, 4), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4),
                    (5, 5), (5, 6)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_left_down(self):
        """
        Tests that coordinates of an upper-left corner get added successfully when looking to the right.
        """
        # Arrange
        side = 'right'
        input_map = main.parse_input('tests/resources/d10_s2_corner_down_right.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (4, 3), (4, 4), (4, 5), (5, 2), (5, 3),
                    (5, 4), (5, 5)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_down_left_down_looking_right(self):
        """
        Tests that corners of type down->left->down are captured when looking to the right.
        """
        # Arrange
        side = 'right'
        input_map = main.parse_input('tests/resources/d10_s2_corner_down_left_down.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4),
                    (5, 3), (5, 4)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_down_right_down(self):
        """
        Tests that corners of type down->right->down are captured when looking to the left.
        """
        # Arrange
        side = 'left'
        input_map = main.parse_input('tests/resources/d10_s2_corner_down_right_down.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(4, 4), (4, 5), (4, 6), (4, 7), (5, 4), (5, 5), (5, 6), (5, 7), (6, 6), (6, 7),
                    (7, 6), (7, 7)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_down_left_down(self):
        """
        Tests that corners of type down->left->down are captured when looking to the left.
        """
        # Arrange
        side = 'left'
        input_map = main.parse_input(
            'tests/resources/d10_s2_corner_down_left_down_looking_left.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 4), (2, 5), (3, 4), (3, 5), (4, 4), (4, 5), (5, 4), (5, 5), (6, 2), (6, 3),
                    (6, 4), (6, 5), (7, 2), (7, 3), (7, 4), (7, 5)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_only_edges_corner_up_left_up(self):
        """
        Tests that corners of type up->left->up are captured when looking to the right.
        """
        # Arrange
        side = 'right'
        input_map = main.parse_input('tests/resources/d10_s2_corner_up_left_up_looking_right.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        diffs = main.to_differences(loop_coords)
        expected = {(2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6),
                    (5, 5), (5, 6), (6, 5), (6, 6)}

        # Act
        actual = main.get_internal_and_border_points(diffs, side)
        actual = actual - set(loop_coords)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_internal_points(self):
        """
        Tests that inner points are also captured.
        """
        # Arrange
        input_map = main.parse_input('tests/resources/d10_internal_points.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        internal_to_border_points = main.get_internal_and_border_points(
            main.to_differences(loop_coords), 'right')
        expected = {(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 2), (3, 3), (3, 4), (3, 5),
                    (3, 6), (3, 7), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (5, 3),
                    (5, 4), (5, 5), (5, 6), (5, 7), (6, 2), (6, 3), (6, 4), (7, 2), (7, 3), (7, 4)}

        # Act
        actual = main.add_inner_points(internal_to_border_points, loop_coords, input_map)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_internal_points_no_internal_points(self):
        """
        Tests that when there are no inner points nothing new gets added
        """
        # Arrange
        input_map = main.parse_input('tests/resources/d10_s1.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        internal_to_border_points = main.get_internal_and_border_points(
            main.to_differences(loop_coords), 'right')
        expected = {(2, 2)}

        # Act
        actual = main.add_inner_points(internal_to_border_points, loop_coords, input_map)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_loop_coords_with_difference_internal_points_start_point_is_entirely_surrounded(self):
        """
        Tests that inner points are also captured even if we have islands of them.
        """
        # Arrange
        input_map = main.parse_input('tests/resources/d10_internal_points_start_surrounded.txt')
        loop_coords = main.get_loop_coordinates(input_map, main.find_start(input_map))
        internal_to_border_points = main.get_internal_and_border_points(
            main.to_differences(loop_coords), 'right')
        expected = {
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (2, 6),
            (2, 7),
            (2, 8),
            (2, 9),
            (3, 2),
            (3, 3),
            (3, 4),
            (3, 5),
            (3, 6),
            (3, 7),
            (3, 8),
            (3, 9),
            (4, 2),
            (4, 3),
            (4, 4),
            (4, 5),
            (4, 6),
            (4, 7),
            (4, 8),
            (4, 9),
            (5, 2),
            (6, 2),
            (7, 2),
            (7, 7),
            (7, 8),
            (7, 9),
            (8, 2),
            (8, 7),
            (8, 8),
            (8, 9),
            (9, 2),
            (9, 7),
            (9, 8),
            (9, 9),
        }

        # Act
        actual = main.add_inner_points(internal_to_border_points, loop_coords, input_map)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected: {expected}. Got: {actual}')

    def test_get_candidates(self):
        """
        Tests that points near the border are identified correctly.
        """
        # Arrange
        sides = ['right', 'right']
        inputs = [
            [((1, 1), (1, 2), (0, 1)), ((1, 2), (1, 3), (0, 1)), ((1, 3), (2, 3), (1, 0)),
             ((2, 3), (3, 3), (1, 0)), ((3, 3), (3, 2), (0, -1)), ((3, 2), (3, 1), (0, -1)),
             ((3, 1), (2, 1), (-1, 0)), ((2, 1), (1, 1), (-1, 0))],
            [((1, 1), (1, 2), (0, 1)), ((1, 2), (1, 3), (0, 1)), ((1, 3), (1, 4), (0, 1)),
             ((1, 4), (1, 5), (0, 1)), ((1, 5), (1, 6), (0, 1)), ((1, 6), (1, 7), (0, 1)),
             ((1, 7), (1, 8), (0, 1)), ((1, 8), (2, 8), (1, 0)), ((2, 8), (3, 8), (1, 0)),
             ((3, 8), (4, 8), (1, 0)), ((4, 8), (5, 8), (1, 0)), ((5, 8), (6, 8), (1, 0)),
             ((6, 8), (7, 8), (1, 0)), ((7, 8), (7, 7), (0, -1)), ((7, 7), (7, 6), (0, -1)),
             ((7, 6), (7, 5), (0, -1)), ((7, 5), (6, 5), (-1, 0)), ((6, 5), (5, 5), (-1, 0)),
             ((5, 5), (5, 6), (0, 1)), ((5, 6), (5, 7), (0, 1)), ((5, 7), (4, 7), (-1, 0)),
             ((4, 7), (3, 7), (-1, 0)), ((3, 7), (2, 7), (-1, 0)), ((2, 7), (2, 6), (0, -1)),
             ((2, 6), (2, 5), (0, -1)), ((2, 5), (2, 4), (0, -1)), ((2, 4), (2, 3), (0, -1)),
             ((2, 3), (2, 2), (0, -1)), ((2, 2), (3, 2), (1, 0)), ((3, 2), (4, 2), (1, 0)),
             ((4, 2), (5, 2), (1, 0)), ((5, 2), (5, 3), (0, 1)), ((5, 3), (5, 4), (0, 1)),
             ((5, 4), (6, 4), (1, 0)), ((6, 4), (7, 4), (1, 0)), ((7, 4), (7, 3), (0, -1)),
             ((7, 3), (7, 2), (0, -1)), ((7, 2), (7, 1), (0, -1)), ((7, 1), (6, 1), (-1, 0)),
             ((6, 1), (5, 1), (-1, 0)), ((5, 1), (4, 1), (-1, 0)), ((4, 1), (3, 1), (-1, 0)),
             ((3, 1), (2, 1), (-1, 0)), ((2, 1), (1, 1), (-1, 0))],
        ]
        expecteds = [
            {(2, 2)},
            {(6, 2), (6, 3), (6, 6), (6, 7)},
        ]

        # Act
        actuals = [
            main.get_internal_and_border_points(difference, side)
            for (difference, side) in zip(inputs, sides)
        ]
        actuals = [
            actual - {p1
                      for p1, _, _ in inp} - {p2
                                              for _, p2, _ in inp}
            for actual, inp in zip(actuals, inputs)
        ]

        # Assert
        self.assertListEqual(actuals, expecteds, f'Expected: {expecteds}. Got: {actuals}')

    def test_determine_side(self):
        """
        Test that the side towards which to consider points as internal to the border is correctly determined.
        """
        # Arrange
        expectations = [
            (main.get_loop_coordinates(main.parse_input(f'tests/resources/{filename}')),
             expected_side) for filename, expected_side in [
                 ('d10_s1.txt', 'right'),
                 ('d10_s1_multiple.txt', 'right'),
                 ('d10_s2.txt', 'right'),
                 ('d10_s4.txt', 'right'),
                 ('d10_internal_points.txt', 'right'),
                 ('d10_s2_corner_down_left_down.txt', 'right'),
                 ('d10_s2_corner_right_up.txt', 'right'),
                 ('d10_s2_corner_left_up.txt', 'left'),
                 ('d10_s2_corner_up_left_up_looking_right.txt', 'right'),
                 ('d10_s2_corner_down_right_down.txt', 'left'),
                 ('d10_s2_corner_up_right.txt', 'left'),
                 ('d10_s2_corner_down_right.txt', 'right'),
                 ('d10_s2_corner_down_left_down_looking_left.txt', 'left'),
                 ('d10_tricky.txt', 'left'),
             ]
        ]

        for idx, (loop_coords, expected_side) in enumerate(expectations):
            # Act
            actual_side = main.determine_side(loop_coords)

            # Assert
            self.assertEqual(
                actual_side, expected_side,
                f'Test case {idx:02d}: For {loop_coords=} expected to get "{expected_side}", but got "{actual_side}".'
            )

    def test_display_map(self):
        """
        Test that two strings that can be used to visualize the loop can also be produced.

        Useful for debugging!
        """
        # Arrange
        input_map = main.parse_input('tests/resources/d10_internal_points_start_surrounded.txt')
        loop_coords = main.get_loop_coordinates(input_map)
        inner_points = main.add_inner_points(
            main.get_internal_and_border_points(main.to_differences(loop_coords),
                                                main.determine_side(loop_coords)), loop_coords,
            input_map)
        expected_before = '            \n S--------7 \n |████████| \n |████████| \n |████████| \n |█F------J \n |█|  F---7 \n |█|  |███| \n |█|  |███| \n |█L--J███| \n L--------J \n            '
        expected_after = '            \n S────────┐ \n │IIIIIIII│ \n │IIIIIIII│ \n │IIIIIIII│ \n │I┌──────┘ \n │I│  ┌───┐ \n │I│  │III│ \n │I│  │III│ \n │I└──┘III│ \n └────────┘ \n            '

        # Act
        before, after = main.display_map(input_map, loop_coords, inner_points)

        # Assert
        self.assertEqual(before, expected_before)
        self.assertEqual(after, expected_after)

    def test_part2(self):
        """
        Tests that part 2 returns the correct number of enclosed points.
        """
        # Arrange
        expectations = [
            ('tests/resources/d10_s1.txt', 1),
            ('tests/resources/d10_s1_multiple.txt', 9),
            ('tests/resources/d10_s2.txt', 4),
            ('tests/resources/d10_s4.txt', 1),
            ('tests/resources/d10_internal_points.txt', 30),
            ('tests/resources/d10_s2_corner_down_left_down.txt', 12),
            ('tests/resources/d10_s2_corner_right_up.txt', 12),
            ('tests/resources/d10_s2_corner_left_up.txt', 12),
            ('tests/resources/d10_s2_corner_up_left_up_looking_right.txt', 14),
            ('tests/resources/d10_s2_corner_down_right_down.txt', 12),
            ('tests/resources/d10_s2_corner_up_right.txt', 12),
            ('tests/resources/d10_s2_corner_down_right.txt', 12),
            ('tests/resources/d10_s2_corner_down_left_down_looking_left.txt', 16),
            ('tests/resources/d10_tricky.txt', 10),
            ('tests/resources/d10_bigger.txt', 10),
            ('tests/resources/d10_bigger2.txt', 8),
            ('tests/resources/d10_up_tricky.txt', 8),
            ('aoc_2023/day10/sample.txt', 1),
            ('aoc_2023/day10/input.txt', 459),
        ]

        for idx, (filename, expected_side) in enumerate(expectations):
            # Act
            actual_side = main.part2(filename)

            # Assert
            self.assertEqual(
                actual_side, expected_side,
                f'Test case {idx:02d}: For "{filename}" expected to get "{expected_side}", but got "{actual_side}".'
            )
