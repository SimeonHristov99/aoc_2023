from __future__ import annotations

import unittest

from aoc_2023.day05.main import move


class TestStringMethods(unittest.TestCase):

    def test_move_no_overlap_right_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the right, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, -1)
        range_ = (1, 10)
        mapping = (11, 13)

        expected_leftover = [range_]

        # Act
        actual_done, actual_leftover = move(destination, mapping, range_)

        # Assert
        self.assertIsNone(
            actual_done,
            f'ERROR: Expected `actual_done=None`, but got `{actual_done=}`',
        )
        self.assertListEqual(
            actual_leftover,
            expected_leftover,
            f'ERROR: Expected `actual_leftover=expected_leftover`, but got `{actual_leftover=}` and `{expected_leftover=}`',
        )

    def test_move_no_overlap_left_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the left, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, -1)
        range_ = (1, 10)
        mapping = (-5, 0)

        expected_leftover = [range_]

        # Act
        actual_done, actual_leftover = move(destination, mapping, range_)

        # Assert
        self.assertIsNone(
            actual_done,
            f'ERROR: Expected `actual_done=None`, but got `{actual_done=}`',
        )
        self.assertListEqual(
            actual_leftover,
            expected_leftover,
            f'ERROR: Expected `actual_leftover=expected_leftover`, but got `{actual_leftover=}` and `{expected_leftover=}`',
        )

    def test_move_overlap_right_results_in_one_done_and_one_to_process(self):
        """
        If there is an overlap to the right, then the passed range should get split in two:
            - the left part should be unchanged and should end at `map[0] - 1`;
            - the right part should be mapped accordingly.
        """
        # Arrange
        expected_done = (52, 57)
        expected_leftover = [(1, 4)]

        line = (1, 10)
        mapping = (5, 15)
        destination = (52, 62)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `actual_done=expected_done`, but got `{actual_done=}` and `{expected_done=}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_right_ending(self):
        """
        If there is an overlap at the right-most element it also gets mapped.
        """
        # Arrange
        expected_done = (52, 55)
        expected_leftover = [(1, 6)]

        line = (1, 10)
        mapping = (7, 10)
        destination = (52, 55)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_right_edge(self):
        """
        Tests that if the map starts at the right-most element, only it gets processed.
        """
        # Arrange
        expected_done = (52, 52)
        expected_leftover = [(1, 9)]

        line = (1, 10)
        mapping = (10, 15)
        destination = (52, 57)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_left_ending(self):
        """
        If there is an overlap at the left-most element it also gets mapped.
        """
        # Arrange
        expected_done = (52, 55)
        expected_leftover = [(4, 10)]

        line = (1, 10)
        mapping = (1, 3)
        destination = (52, 55)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_left_edge(self):
        """
        Tests that if the map ends at the left-most element, only it gets processed.
        """
        # Arrange
        expected_done = (58, 58)
        expected_leftover = [(2, 10)]

        line = (1, 10)
        mapping = (-5, 1)
        destination = (52, 58)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_left_results_in_one_done_and_one_to_process(self):
        """
        If there is an overlap to the left, then the passed range should get split in two:
            - the left part should be mapped accordingly;
            - the right part should remain unchanged.
        """
        # Arrange
        expected_done = (58, 62)
        expected_leftover = [(6, 10)]

        line = (1, 10)
        mapping = (-5, 5)
        destination = (52, 62)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )

    def test_move_overlap_middle_results_in_one_done_and_two_to_process(self):
        """
        If there is an overlap in middle, i.e. the map is contained in the range/line,
        then the range should get broken down into three parts with the middle part
        being done and the other two being leftover.
        """
        # Arrange
        expected_done = (52, 55)
        expected_leftover = [(1, 2), (7, 10)]

        line = (1, 10)
        mapping = (3, 6)
        destination = (52, 55)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'ERROR: Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'ERROR: Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`'
        )
