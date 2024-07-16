import unittest

import pytest

from aoc_2023.day10 import main


class TestDay10(unittest.TestCase):

    def test_find_one(self):
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
            actuals.append(main.find_one(matrix))

        # Assert
        self.assertListEqual(actuals, expectations)

    def test_find_one_raises_when_no_one(self):
        """
        Tests that an exception is raised when 'S' is not found.
        """
        # Arrange
        matrix = [['-', 'L', '|', 'F', '7'], ['7', 'G', '-', '7', '|']]
        expected_text = 'Coordinates of starting point not found.'

        # Act
        with pytest.raises(NotImplementedError) as exception_context:
            _ = main.find_one(matrix)
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
        actual = main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(actual, expected)

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
        actual = main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(actual, expected)

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
        actual = main.up(coords, stack, seen, path)

        # Assert
        self.assertListEqual(actual, expected)

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
        actual = main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(actual, expected)

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
        actual = main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(actual, expected)

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
        actual = main.down(coords, stack, seen, path, num_rows)

        # Assert
        self.assertListEqual(actual, expected)

    # def test_num_steps_v1(self):
    #     """
    #     Tests that the number of steps to the farthest point is calculated correctly - variant 1.
    #     """
    #     # Arrange
    #     matrix = [
    #         ['-', 'L', '|', 'F', '7'],
    #         ['7', 'S', '-', '7', '|'],
    #         ['L', '|', '7', '|', '|'],
    #         ['-', 'L', '-', 'J', '|'],
    #         ['L', '|', '-', 'J', 'F'],
    #     ]
    #     start_coords = (1, 1)
    #     expected = 4

    #     # Act
    #     actual = main.num_steps_farthest(matrix, start_coords)

    #     # Assert
    #     self.assertEqual(actual, expected)

    # def test_num_steps_v2(self):
    #     """
    #     Tests that the number of steps to the farthest point is calculated correctly - variant 2.
    #     """
    #     # Arrange
    #     matrix = [
    #         ['7', '-', 'F', '7', '-'],
    #         ['.', 'F', 'J', '|', '7'],
    #         ['S', 'J', 'L', 'L', '7'],
    #         ['|', 'F', '-', '-', 'J'],
    #         ['L', 'J', '.', 'L', 'J'],
    #     ]
    #     start_coords = (2, 0)
    #     expected = 8

    #     # Act
    #     actual = main.num_steps_farthest(matrix, start_coords)

    #     # Assert
    #     self.assertEqual(actual, expected)
