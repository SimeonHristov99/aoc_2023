import unittest

from aoc_2023.day08 import main


class TestDay08(unittest.TestCase):

    def test_parsing_input(self):
        """
        Tests that parsing the input returns a tuple with the directions and a dictionary from node to children.
        """
        # Arrange
        filename = 'aoc_2023/day08/sample2.txt'
        expected_directions = 'LLR'
        expected_map = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }

        # Act
        actual_directions, actual_map = main.parse_input(filename)

        # Assert
        self.assertEqual(actual_directions, expected_directions)
        self.assertEqual(actual_map, expected_map)

    def test_get_num_steps_v1(self):
        """
        Tests that obtaining the number of steps works - variant 1.
        """
        # Arrange
        directions = 'LLR'
        map_ = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }
        expected = 6

        # Act
        actual = main.num_steps(directions, map_)

        # Assert
        self.assertEqual(expected, actual)

    def test_get_num_steps_v2(self):
        """
        Tests that obtaining the number of steps works - variant 2.
        """
        # Arrange
        directions = 'RL'
        map_ = {
            'AAA': ('BBB', 'CCC'),
            'BBB': ('DDD', 'EEE'),
            'CCC': ('ZZZ', 'GGG'),
            'DDD': ('DDD', 'DDD'),
            'EEE': ('EEE', 'EEE'),
            'GGG': ('GGG', 'GGG'),
            'ZZZ': ('ZZZ', 'ZZZ'),
        }
        expected = 2

        # Act
        actual = main.num_steps(directions, map_)

        # Assert
        self.assertEqual(expected, actual)

    def test_get_num_ghost_steps(self):
        """
        Tests that obtaining the number of steps when one is a ghost works.
        """
        # Arrange
        directions = 'LR'
        map_ = {
            '11A': ('11B', 'XXX'),
            '11B': ('XXX', '11Z'),
            '11Z': ('11B', 'XXX'),
            '22A': ('22B', 'XXX'),
            '22B': ('22C', '22C'),
            '22C': ('22Z', '22Z'),
            '22Z': ('22B', '22B'),
            'XXX': ('XXX', 'XXX'),
        }
        expected = 6

        # Act
        actual = main.num_ghost_steps(directions, map_)

        # Assert
        self.assertEqual(expected, actual)

    def test_bfs_v1(self):
        """
        Tests that running BFS works for "11A".
        """
        # Arrange
        expected_path_directions = [(['11Z', '11B', '11A'], 'RL')]
        map_ = {
            '11A': ('11B', 'XXX'),
            '11B': ('XXX', '11Z'),
            '11Z': ('11B', 'XXX'),
            '22A': ('22B', 'XXX'),
            '22B': ('22C', '22C'),
            '22C': ('22Z', '22Z'),
            '22Z': ('22B', '22B'),
            'XXX': ('XXX', 'XXX'),
        }

        # Act
        actual_path_directions = main.bfs(map_, '11A')

        # Assert
        self.assertListEqual(actual_path_directions, expected_path_directions)

    def test_bfs_v2(self):
        """
        Tests that running BFS works for "22A".
        """
        # Arrange
        expected_path_directions = [(['22Z', '22C', '22B', '22A'], 'LRL'),
                                    (['22Z', '22C', '22B', '22A'], 'RRL'),
                                    (['22Z', '22C', '22B', '22A'], 'LLL'),
                                    (['22Z', '22C', '22B', '22A'], 'RLL')]
        map_ = {
            '11A': ('11B', 'XXX'),
            '11B': ('XXX', '11Z'),
            '11Z': ('11B', 'XXX'),
            '22A': ('22B', 'XXX'),
            '22B': ('22C', '22C'),
            '22C': ('22Z', '22Z'),
            '22Z': ('22B', '22B'),
            'XXX': ('XXX', 'XXX'),
        }

        # Act
        actual_path_directions = main.bfs(map_, '22A')

        # Assert
        self.assertListEqual(
            sorted(actual_path_directions), sorted(expected_path_directions)
        )

    def test_bfs_does_not_repeat_goal_node(self):
        """
        Tests that running BFS will not append the goal node more than one time to the resulting paths.
        """
        # Arrange
        expected_path_directions = [
            (['ZZZ', 'BBB', 'AAA'], 'RL'),
            (['ZZZ', 'BBB', 'AAA'], 'RR'),
        ]
        map_ = {
            'AAA': ('BBB', 'BBB'),
            'BBB': ('AAA', 'ZZZ'),
            'ZZZ': ('ZZZ', 'ZZZ')
        }

        # Act
        actual_path_directions = main.bfs(map_, 'AAA')

        # Assert
        self.assertListEqual(
            sorted(actual_path_directions), sorted(expected_path_directions)
        )

    def test_get_steps_v1(self):
        """
        Tests that the number of steps can be correctly calculated given a pattern and correct paths - variant 1.
        """
        # Arrange
        expected_num_steps = 6
        pattern = 'LLR'
        paths = {'LR', 'RR'}

        # Act
        actual_num_steps = main.get_steps(pattern, paths)

        # Assert
        self.assertEqual(actual_num_steps, expected_num_steps)

    def test_get_steps_v2(self):
        """
        Tests that the number of steps can be correctly calculated given a pattern and correct paths - variant 2.
        """
        # Arrange
        expected_num_steps = 2
        pattern = 'RL'
        paths = {'RL'}

        # Act
        actual_num_steps = main.get_steps(pattern, paths)

        # Assert
        self.assertEqual(actual_num_steps, expected_num_steps)
