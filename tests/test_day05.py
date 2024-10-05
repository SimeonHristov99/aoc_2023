from __future__ import annotations

import unittest

from aoc_2023.day05.main import almanac, apply_map, move


class TestDay05(unittest.TestCase):

    def test_move_point(self):
        """
        Tests that move can be used to map a single point, contained in the mapping.
        """
        # Arrange
        expected_done = (47, 47)
        expected_leftover = []

        line = (6, 6)
        mapping = (1, 10)
        destination = (42, 51)

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertEqual(
            actual_done,
            expected_done,
            f'Expected `actual_done=expected_done`, but got `{actual_done=}` and `{expected_done=}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

    def test_move_no_overlap_right_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the right, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, 1)
        line = (1, 10)
        mapping = (11, 13)

        expected_leftover = [line]

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertIsNone(
            actual_done,
            f'Expected `actual_done=None`, but got `{actual_done=}`',
        )
        self.assertListEqual(
            actual_leftover,
            expected_leftover,
            f'Expected `actual_leftover=expected_leftover`, but got `{actual_leftover=}` and `{expected_leftover=}`',
        )

    def test_move_no_overlap_left_leaves_without_changes(self):
        """
        If there is no overlap and the map is to the left, nothing should be done and the range should remain unchanged.
        """
        # Arrange
        destination = (-1, 4)
        line = (1, 10)
        mapping = (-5, 0)

        expected_leftover = [line]

        # Act
        actual_done, actual_leftover = move(destination, mapping, line)

        # Assert
        self.assertIsNone(
            actual_done,
            f'Expected `actual_done=None`, but got `{actual_done=}`',
        )
        self.assertListEqual(
            actual_leftover,
            expected_leftover,
            f'Expected `actual_leftover=expected_leftover`, but got `{actual_leftover=}` and `{expected_leftover=}`',
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
            f'Expected `actual_done=expected_done`, but got `{actual_done=}` and `{expected_done=}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
            f'Expected `done={expected_done}`, but got `done={actual_done}`',
        )
        self.assertListEqual(
            actual_leftover, expected_leftover,
            f'Expected `leftover={expected_leftover}`, but got `leftover={actual_leftover}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_apply_map_returns_only_needed_ranges(self):
        """
        Tests that apply map does not return ranges that were not requested.
        """
        # Arrange
        expected = {(43, 43)}

        line = (2, 2)
        map_ = {42: (1, 9)}

        # Act
        actual = apply_map(map_, line)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_two_times(self):
        """
        Tests that almanac can be used to map one seed 2 times (soil to fertilizer).
        """
        # Arrange
        expected = {(52, 52)}

        line = (13, 13)
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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_three_times(self):
        """
        Tests that almanac can be used to map one seed 3 times (fertilizer to water).
        """
        # Arrange
        expected = {(41, 41)}

        seed = (13, 13)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_four_times(self):
        """
        Tests that almanac can be used to map one seed 4 times (water to light).
        """
        # Arrange
        expected = {(34, 34)}

        seed = (13, 13)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_five_times(self):
        """
        Tests that almanac can be used to map one seed 5 times (light to temperature).
        """
        # Arrange
        expected = {(34, 34)}

        seed = (13, 13)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
            {
                45: (77, 23),
                81: (45, 19),
                68: (64, 13),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_six_times(self):
        """
        Tests that almanac can be used to map one seed 6 times (temperature to humidity).
        """
        # Arrange
        expected = {(35, 35)}

        seed = (13, 13)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
            {
                45: (77, 23),
                81: (45, 19),
                68: (64, 13),
            },
            {
                0: (69, 1),
                1: (0, 69),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_one_seven_times(self):
        """
        Tests that almanac can be used to map one seed 7 times (humidity to location).
        """
        # Arrange
        expected = {(35, 35)}

        seed = (13, 13)
        maps = [{
            50: (98, 2),
            52: (50, 48)
        }, {
            0: (15, 37),
            37: (52, 2),
            39: (0, 15)
        }, {
            49: (53, 8),
            0: (11, 42),
            42: (0, 7),
            57: (7, 4),
        }, {
            88: (18, 7),
            18: (25, 70),
        }, {
            45: (77, 23),
            81: (45, 19),
            68: (64, 13),
        }, {
            0: (69, 1),
            1: (0, 69),
        }, {
            60: (56, 37),
            56: (93, 4),
        }]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_two_times(self):
        """
        Tests that almanac can be used to map one seed 2 times (soil to fertilizer).
        """
        # Arrange
        expected = {(84, 84)}

        line = (82, 82)
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
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_three_times(self):
        """
        Tests that almanac can be used to map one seed 3 times (fertilizer to water).
        """
        # Arrange
        expected = {(84, 84)}

        seed = (82, 82)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_four_times(self):
        """
        Tests that almanac can be used to map one seed 4 times (water to light).
        """
        # Arrange
        expected = {(77, 77)}

        seed = (82, 82)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_five_times(self):
        """
        Tests that almanac can be used to map one seed 5 times (light to temperature).
        """
        # Arrange
        expected = {(45, 45)}

        seed = (82, 82)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
            {
                45: (77, 23),
                81: (45, 19),
                68: (64, 13),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_six_times(self):
        """
        Tests that almanac can be used to map one seed 6 times (temperature to humidity).
        """
        # Arrange
        expected = {(46, 46)}

        seed = (82, 82)
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
            {
                49: (53, 8),
                0: (11, 42),
                42: (0, 7),
                57: (7, 4),
            },
            {
                88: (18, 7),
                18: (25, 70),
            },
            {
                45: (77, 23),
                81: (45, 19),
                68: (64, 13),
            },
            {
                0: (69, 1),
                1: (0, 69),
            },
        ]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_can_be_used_to_map_seed_from_part_two_seven_times(self):
        """
        Tests that almanac can be used to map one seed 7 times (humidity to location).
        """
        # Arrange
        expected = {(46, 46)}

        seed = (82, 82)
        maps = [{
            50: (98, 2),
            52: (50, 48)
        }, {
            0: (15, 37),
            37: (52, 2),
            39: (0, 15)
        }, {
            49: (53, 8),
            0: (11, 42),
            42: (0, 7),
            57: (7, 4),
        }, {
            88: (18, 7),
            18: (25, 70),
        }, {
            45: (77, 23),
            81: (45, 19),
            68: (64, 13),
        }, {
            0: (69, 1),
            1: (0, 69),
        }, {
            60: (56, 37),
            56: (93, 4),
        }]

        # Act
        actual = almanac(maps, seed)

        # Assert
        self.assertSetEqual(actual, expected, f'Expected to get `{expected}`, but got `{actual}`')

    def test_almanac_ranges(self):
        """
        Tests that almanac can be used to map a range and the minimum value in the result is 46.
        """
        # Arrange
        expected = 46

        line = (79, 92)
        maps = [{
            50: (98, 2),
            52: (50, 48),
        }, {
            0: (15, 37),
            37: (52, 2),
            39: (0, 15),
        }, {
            49: (53, 8),
            0: (11, 42),
            42: (0, 7),
            57: (7, 4),
        }, {
            88: (18, 7),
            18: (25, 70),
        }, {
            45: (77, 23),
            81: (45, 19),
            68: (64, 13),
        }, {
            0: (69, 1),
            1: (0, 69),
        }, {
            60: (56, 37),
            56: (93, 4),
        }]

        # Act
        mapped_ranges = almanac(maps, line)
        actual = float('inf')
        for mapped_range in mapped_ranges:
            actual = min(actual, mapped_range[0])

        # Assert
        self.assertEqual(actual, expected, f'Expected to get {expected}, but got {actual}.')
