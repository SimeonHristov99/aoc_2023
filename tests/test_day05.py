from __future__ import annotations

import unittest

from aoc_2023.day05.main import almanac, apply_map, move


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

    def test_apply_map_two_ranges_basic(self):
        """
        Tests that a map with two mappings can be applied accordingly when the maps are contained in the line.
        """
        # Arrange
        expected = {(1, 2), (52, 54), (6, 6), (100, 102), (10, 10)}

        line = (1, 10)
        map_ = {52: (3, 3), 100: (7, 3)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_apply_map_two_ranges_longer_maps(self):
        """
        Tests that a map with two mappings can be applied accordingly when the maps are not contained in the line.
        """
        # Arrange
        expected = {(16, 19), (5, 5), (40, 44)}

        line = (1, 10)
        maps = {10: (-5, 10), 40: (6, 10)}

        # Act
        actual = apply_map(maps, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_apply_map_order_does_not_matter(self):
        """
        Tests that the order in which mappings are applied does not matter.
        Here the last mapping covers the first segment of the line.
        """
        # Arrange
        expected = {(40, 41), (52, 54), (6, 6), (100, 102), (10, 10)}

        line = (1, 10)
        map_ = {52: (3, 3), 100: (7, 3), 40: (1, 2)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_apply_map_ranges_cover_line(self):
        """
        Tests that applying a map that has ranges covering all of the line works.
        """
        # Arrange
        expected = {(40, 41), (52, 55), (100, 103)}

        line = (1, 10)
        map_ = {52: (3, 4), 100: (7, 4), 40: (1, 2)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_apply_map_non_overlapping_leaves_line_unchanged(self):
        """
        Tests that if a map contains no ranges that cover the line,
        the line is unaltered.
        """
        # Arrange
        expected = {(1, 10)}

        line = (1, 10)
        map_ = {52: (11, 2), 40: (-5, 2)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_move_does_not_produce_invalid_points(self):
        """
        Tests that move does not produce points that have second coordinate smaller than the first.
        """
        # Arrange
        expected = {(35, 36)}

        line = (50, 51)
        map_ = {0: (15, 37), 37: (52, 2), 39: (0, 15)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )

    def test_almanac_two_maps(self):
        """
        Tests that applying almanac with the maps works.
        """
        # Arrange
        expected = {(39, 53), (0, 34), (37, 38), (54, 99), (35, 36)}

        line = (0, 99)
        maps = [
            {
                50: (98, 2),
                52: (50, 48)
            },
            {
                0: (15, 37),
                37: (52, 2),
                39: (0, 15)
            },
        ]

        # Act
        actual = almanac(maps, line)

        # Assert
        self.assertSetEqual(
            actual, expected,
            f'ERROR: Expected to get `{expected}`, but got `{actual}`'
        )
