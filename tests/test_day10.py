import unittest

import pytest

from aoc_2023.day10 import main


class TestDay10(unittest.TestCase):

    def test_parse_input(self):
        """
        Tests that the input is parsed correctly.
        """
        # Arrange
        filename = 'aoc_2023/day10/sample1.txt'
        expected = [
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ]

        # Act
        actual = main.parse_input(filename)

        # Assert
        self.assertListEqual(actual, expected)

    def test_find_start(self):
        """
        Tests that the coordinates of the starting point are correctly found.
        """
        # Arrange
        matrices = [[
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ],
                    [
                        ['7', '-', 'F', '7', '-'],
                        ['.', 'F', 'J', '|', '7'],
                        ['S', 'J', 'L', 'L', '7'],
                        ['|', 'F', '-', '-', 'J'],
                        ['L', 'J', '.', 'L', 'J'],
                    ]]
        expectations = [(1, 1), (2, 0)]
        actuals = []

        # Act
        for matrix in matrices:
            actuals.append(main.find_start(matrix))

        # Assert
        self.assertListEqual(actuals, expectations)

    def test_find_start_raises_when_no_one(self):
        """
        Tests that an exception is raised when 'S' is not found.
        """
        # Arrange
        matrix = [['-', 'L', '|', 'F', '7'], ['7', 'G', '-', '7', '|']]
        expected_text = 'Coordinates of starting point not found.'

        # Act
        with pytest.raises(NotImplementedError) as exception_context:
            _ = main.find_start(matrix)
        actual_text = str(exception_context.value)

        # Assert
        self.assertEqual(actual_text, expected_text)

    def test_up_can_move_adds_new_coords(self):
        """
        Tests that moving up works when x is greater than 0.
        """
        # Arrange
        coords = (1, 1)
        stack = []
        path = [(5, 6)]
        seen = set()
        expected = [[(5, 6), (0, 1)]]

        # Act
        main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_up_cannot_move_does_not_add(self):
        """
        Tests that moving up does not add a new coordinate when x is 0.
        """
        # Arrange
        coords = (0, 1)
        stack = []
        path = []
        seen = set()
        expected = []

        # Act
        main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_up_can_move_does_not_add_when_seen(self):
        """
        Tests that moving up does not add new coordinates when they have been seen.
        """
        # Arrange
        coords = (1, 1)
        stack = []
        path = []
        seen = {(0, 1)}
        expected = []

        # Act
        main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_down_can_move_adds_new_coords(self):
        """
        Tests that moving down works when x is less than the number of rows.
        """
        # Arrange
        num_rows = 2
        coords = (0, 1)
        stack = []
        path = [(4, 8)]
        seen = set()
        expected = [[(4, 8), (1, 1)]]

        # Act
        main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(stack, expected)

    def test_down_cannot_move_does_not_add(self):
        """
        Tests that moving down does not add a new coordinate when x is the last row.
        """
        # Arrange
        num_rows = 2
        coords = (1, 1)
        stack = []
        path = []
        seen = set()
        expected = []

        # Act
        main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(stack, expected)

    def test_down_can_move_does_not_add_when_seen(self):
        """
        Tests that moving down does not add new coordinates when they have been seen.
        """
        # Arrange
        num_rows = 2
        coords = (0, 1)
        stack = []
        path = []
        seen = {(1, 1)}
        expected = []

        # Act
        main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(stack, expected)

    def test_left_can_move_adds_new_coords(self):
        """
        Tests that moving left works when y is greater than 0.
        """
        # Arrange
        coords = (1, 1)
        stack = []
        path = [(5, 6)]
        seen = set()
        expected = [[(5, 6), (1, 0)]]

        # Act
        main.left(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_left_cannot_move_does_not_add(self):
        """
        Tests that moving left does not add a new coordinate when y is 0.
        """
        # Arrange
        coords = (1, 0)
        stack = []
        path = []
        seen = set()
        expected = []

        # Act
        main.left(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_left_can_move_does_not_add_when_seen(self):
        """
        Tests that moving left does not add new coordinates when they have been seen.
        """
        # Arrange
        coords = (1, 1)
        stack = []
        path = []
        seen = {(1, 0)}
        expected = []

        # Act
        main.left(coords, stack, seen, path)

        # Assert
        self.assertListEqual(stack, expected)

    def test_right_can_move_adds_new_coords(self):
        """
        Tests that moving right works when y is less than the number of columns.
        """
        # Arrange
        num_cols = 2
        coords = (0, 0)
        stack = []
        path = [(4, 8)]
        seen = set()
        expected = [[(4, 8), (0, 1)]]

        # Act
        main.right(coords, stack, seen, path, num_cols)

        # Assert
        self.assertListEqual(stack, expected)

    def test_right_cannot_move_does_not_add(self):
        """
        Tests that moving right does not add a new coordinate when y is the last column.
        """
        # Arrange
        num_cols = 2
        coords = (1, 1)
        stack = []
        path = []
        seen = set()
        expected = []

        # Act
        main.right(coords, stack, seen, path, num_cols)

        # Assert
        self.assertListEqual(stack, expected)

    def test_right_can_move_does_not_add_when_seen(self):
        """
        Tests that moving right does not add new coordinates when they have been seen.
        """
        # Arrange
        num_cols = 2
        coords = (0, 0)
        stack = []
        path = []
        seen = {(0, 1)}
        expected = []

        # Act
        main.right(coords, stack, seen, path, num_cols)

        # Assert
        self.assertListEqual(stack, expected)

    def test_initiate_stack(self):
        """
        Tests that all possible paths get added to the stack initially.
        """
        # Arrange
        matrix = [
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ]
        start_coords = (1, 1)
        expected = [[(1, 1), (2, 1)], [(1, 1), (1, 2)]]

        # Act
        actual = main.initialize_stack(matrix, start_coords)

        # Assert
        self.assertEqual(actual, expected)

    def test_num_steps_v1(self):
        """
        Tests that the number of steps to the farthest point is calculated correctly - variant 1.
        """
        # Arrange
        matrix = [
            ['-', 'L', '|', 'F', '7'],
            ['7', 'S', '-', '7', '|'],
            ['L', '|', '7', '|', '|'],
            ['-', 'L', '-', 'J', '|'],
            ['L', '|', '-', 'J', 'F'],
        ]
        start_coords = (1, 1)
        expected = 4

        # Act
        actual = main.num_steps_farthest(matrix, start_coords)

        # Assert
        self.assertEqual(actual, expected)

    def test_num_steps_v2(self):
        """
        Tests that the number of steps to the farthest point is calculated correctly - variant 2.
        """
        # Arrange
        matrix = [
            ['7', '-', 'F', '7', '-'],
            ['.', 'F', 'J', '|', '7'],
            ['S', 'J', 'L', 'L', '7'],
            ['|', 'F', '-', '-', 'J'],
            ['L', 'J', '.', 'L', 'J'],
        ]
        start_coords = (2, 0)
        expected = 8

        # Act
        actual = main.num_steps_farthest(matrix, start_coords)

        # Assert
        self.assertEqual(actual, expected)

    def test_part1(self):
        """
        Tests that part 1 works for the samples and input.
        """
        # Arrange
        fs = [
            'aoc_2023/day10/sample1.txt', 'aoc_2023/day10/sample2.txt',
            'aoc_2023/day10/input.txt'
        ]
        expectations = [4, 8, 6828]

        # Act
        actuals = [main.part1(filename) for filename in fs]

        # Assert
        self.assertListEqual(actuals, expectations)
