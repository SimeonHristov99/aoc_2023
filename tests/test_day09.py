import unittest

from aoc_2023.day09 import main


class TestDay09(unittest.TestCase):

    def test_parsing(self):
        """
        Tests that parsing works.
        """
        # Arrange
        filename = 'aoc_2023/day09/sample.txt'
        expected = [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21],
                    [10, 13, 16, 21, 30, 45]]

        # Act
        actual = main.parse_input(filename)

        # Assert
        self.assertListEqual(actual, expected)

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

    def test_predict_left_v1(self):
        """
        Tests that predicting the first number works - variant 1.
        """
        # Arrange
        xs = [-3, 0, 3, 6, 9, 12, 15]
        expected = 18

        # Act
        actual = main.predict(xs)

        # Assert
        self.assertEqual(actual, expected)

    def test_predict_left_v2(self):
        """
        Tests that predicting the first number works - variant 2.
        """
        # Arrange
        expected = 28
        xs = [0, 1, 3, 6, 10, 15, 21]

        # Act
        actual = main.predict(xs)

        # Assert
        self.assertEqual(actual, expected)

    def test_predict_left_v3(self):
        """
        Tests that predicting the first number works - variant 3.
        """
        # Arrange
        xs = [10, 13, 16, 21, 30, 45]
        expected = 5

        # Act
        actual = main.predict(xs, left=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_part1_sample(self):
        """
        Tests that passing the sample for part 1 works.
        """
        # Arrange
        filename = 'aoc_2023/day09/sample.txt'
        expected = 114

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)

    def test_part1_input(self):
        """
        Tests that passing the input for part 1 works.
        """
        # Arrange
        filename = 'aoc_2023/day09/input.txt'
        expected = 1743490457

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)
