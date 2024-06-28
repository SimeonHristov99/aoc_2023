import unittest

from aoc_2023.day06.main import get_bigger_distances


class TestDay06(unittest.TestCase):

    def test_get_bigger_distances_threshold_v1(self):
        """
        Tests that the correct number of distances larger than a threshold are returned - variant 1.
        """
        # Arrange
        time = 7
        threshold = 9
        expected = 4

        # Act
        actual = get_bigger_distances(time, threshold)

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
        actual = get_bigger_distances(time, threshold)

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
        actual = get_bigger_distances(time, threshold)

        # Assert
        self.assertEqual(
            actual, expected,
            f'For {time=} and {threshold=}, expected to get {expected} ways in which to surpass the threshold, but got {actual}.'
        )
