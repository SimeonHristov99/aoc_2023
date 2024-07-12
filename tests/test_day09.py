import unittest

from aoc_2023.day09 import main


class TestDay09(unittest.TestCase):

    def test_predict_v1(self):
        """
        Tests that predicting the next number works - variant 1.
        """
        # Arrange
        expected = 18
        xs = [0, 3, 6, 9, 12, 15]

        # Act
        actual = main.predict(xs)

        # Assert
        self.assertEqual(actual, expected)

    def test_predict_v2(self):
        """
        Tests that predicting the next number works - variant 2.
        """
        # Arrange
        expected = 28
        xs = [1, 3, 6, 10, 15, 21]

        # Act
        actual = main.predict(xs)

        # Assert
        self.assertEqual(actual, expected)

    def test_predict_v3(self):
        """
        Tests that predicting the next number works - variant 3.
        """
        # Arrange
        expected = 68
        xs = [10, 13, 16, 21, 30, 45]

        # Act
        actual = main.predict(xs)

        # Assert
        self.assertEqual(actual, expected)
