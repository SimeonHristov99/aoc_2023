from __future__ import annotations

import unittest

from aoc_2023.day05.main import move


class TestStringMethods(unittest.TestCase):

    def test_mapping_no_overlap_right_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the right, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, -1)
        range_ = (1, 10)
        map_ = (11, 13)

        expected_leftover = [range_]

        # Act
        actual_done, actual_leftover = move(destination, map_, range_)

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

    def test_mapping_no_overlap_left_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the left, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, -1)
        range_ = (1, 10)
        map_ = (-5, 0)

        expected_leftover = [range_]

        # Act
        actual_done, actual_leftover = move(destination, map_, range_)

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

    def test_mapping_overlap_right_results_in_one_done_and_one_to_process(
        self
    ):
        """
        If there is an overlap to the right, then the passed range should get split in two:
            - the left part should be unchanged and should end at `map[0] - 1`
            - the right part should be mapped accordingly.
        """
        # Arrange
        expected_done = (52, 57)
        expected_leftover = [(1, 4)]

        line = (1, 10)
        map_ = (5, 15)
        destination = (52, 62)

        # Act
        actual_done, actual_leftover = move(destination, map_, line)

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

    def test_mapping_overlap_left_results_in_one_done_and_one_to_process(self):
        """
        If there is an overlap to the right, then the passed range should get split in two:
            - the left part should be unchanged and should end at `map[0] - 1`
            - the right part should be mapped accordingly.
        """
        # Arrange
        expected_done = (52, 57)
        expected_leftover = [(1, 4)]

        line = (1, 10)
        map_ = (5, 15)
        destination = (52, 62)

        # Act
        actual_done, actual_leftover = move(destination, map_, line)

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

    # def test_mapping_overlap_middle_results_in_one_done_and_two_to_process(self):
    #     # Arrange

    #     # Act

    #     # Assert
    #     assert False
