import unittest

from aoc_2023.day06 import main


class TestDay06(unittest.TestCase):

    def test_input_parsing_part1(self):
        """
        Tests that the input can be parsed according to the requirements of part 1.
        """
        # Arrange
        input_file = 'aoc_2023/day06/sample.txt'
        expected = [(7, 9), (15, 40), (30, 200)]

        # Act
        actual = main.parse_input(input_file)

        # Assert
        self.assertListEqual(actual, expected, f'Expected to get {expected}, but got {actual}.')

    def test_get_bigger_distances_threshold_v1(self):
        """
        Tests that the correct number of distances larger than a threshold are returned - variant 1.
        """
        # Arrange
        time = 7
        threshold = 9
        expected = 4

        # Act
        actual = main.get_bigger_distances(time, threshold)

        # Assert
        self.assertEqual(
            actual, expected,
            f'For {time=} and {threshold=}, expected to get {expected} ways in which to surpass the threshold, but got {actual}.'
        )

    def test_get_bigger_distances_threshold_v2(self):
        """
        Tests that the correct number of distances larger than a threshold are returned - variant 2.
        """
        # Arrange
        time = 15
        threshold = 40
        expected = 8

        # Act
        actual = main.get_bigger_distances(time, threshold)

        # Assert
        self.assertEqual(
            actual, expected,
            f'For {time=} and {threshold=}, expected to get {expected} ways in which to surpass the threshold, but got {actual}.'
        )

    def test_get_bigger_distances_threshold_v3(self):
        """
        Tests that the correct number of distances larger than a threshold are returned - variant 3.
        """
        # Arrange
        time = 30
        threshold = 200
        expected = 9

        # Act
        actual = main.get_bigger_distances(time, threshold)

        # Assert
        self.assertEqual(
            actual, expected,
            f'For {time=} and {threshold=}, expected to get {expected} ways in which to surpass the threshold, but got {actual}.'
        )

    def test_input_parsing_part2(self):
        """
        Tests that the input can be parsed according to the requirements of part 2.
        """
        # Arrange
        input_file = 'aoc_2023/day06/sample.txt'
        expected = (71530, 940200)

        # Act
        actual = main.parse_input_part2(input_file)

        # Assert
        self.assertTupleEqual(actual, expected, f'Expected to get {expected}, but got {actual}.')
