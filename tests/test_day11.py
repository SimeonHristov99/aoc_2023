import unittest

import pytest

from aoc_2023.day11 import main


class TestParse(unittest.TestCase):
    """
    Class for testing the function that parses the input.
    """

    def test_parse_sample(self):
        """
        Tests that the sample is parsed correctly.
        """
        # Arrange
        file = 'aoc_2023/day11/sample.txt'
        expected = [
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ]

        # Act
        actual = main.parse(file)

        # Assert
        self.assertListEqual(actual, expected)


class TestTranspose(unittest.TestCase):
    """
    Class for testing the function that transposes a matrix.
    """

    def test_transpose_sample(self):
        """
        Tests that the function transposes the sample correctly.
        """
        # Arrange
        matrix = [
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ]
        expected = [['.', '.', '#', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
                    ['.', '#', '.', '.', '.', '.', '.', '.', '#', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']]

        # Act
        actual = main.transpose(matrix)

        # Assert
        self.assertListEqual(actual, expected)


class TestGetEmptyLines(unittest.TestCase):
    """
    Class for testing the function that can be used to return the indices of the rows and columns with no galaxies.
    """

    def test_finds_empty_rows_correctly(self):
        """
        Tests that the function returns the correct indices of empty rows.
        """
        # Arrange
        universe = [
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ]
        expected = [3, 7]

        # Act
        actual = main.get_empty_lines(universe, axis=0)

        # Assert
        self.assertListEqual(actual, expected)

    def test_finds_empty_columns_correctly(self):
        """
        Tests that the function returns the correct indices of empty columns.
        """
        # Arrange
        universe = [
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['#', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ]
        expected = [2, 5, 8]

        # Act
        actual = main.get_empty_lines(universe, axis=1)

        # Assert
        self.assertListEqual(actual, expected)

    def test_throws_when_axis_is_not_zero_or_one(self):
        """
        Tests that the function raises an exception when the axis is not 0 or 1.
        """
        # Arrange
        expected_log = 'Axis=100 is not supported. The axis value must be either 0 or 1.'
        excinfo = None

        # Act
        with pytest.raises(ValueError) as excinfo:
            main.get_empty_lines([['.', '.', '.']], 100)

        # Assert
        self.assertIn(expected_log, str(excinfo.value))


class TestExpand(unittest.TestCase):
    """
    Class for testing the function that expands the universe.
    """

    def test_expand_sample_with_coefficient_1(self):
        """
        Tests that the function expands the universe correctly when the coefficient of expansion is 1.
        """
        # Arrange
        coords = [(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 0), (9, 4)]
        expected = [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]

        # Act
        actual = main.expand(coords, 1, [3, 7], [2, 5, 8])

        # Assert
        self.assertListEqual(sorted(actual), sorted(expected))

    # test_expand_sample_with_coefficient_10
    # test_expand_sample_with_coefficient_100
    # test_expand_sample_with_coefficient_1000000


class TestGetGalaxiesCoordinates(unittest.TestCase):
    """
    Class for testing the function that returns the coordinates of the galaxies.
    """

    def test_finds_galaxies_in_sample_correctly(self):
        """
        Tests that the function correctly finds the coordinates of the galaxies in the sample.
        """
        # Arrange
        universe = [
            ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
        ]
        expected_coordinates = [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0),
                                (11, 5)]

        # Act
        actual_coordinates = main.get_galaxy_coordinates(universe)

        # Assert
        self.assertListEqual(actual_coordinates, expected_coordinates)


class TestGetPairs(unittest.TestCase):
    """
    Class for testing the function that returns the pairs for which the distance has to be calculated.
    """

    def test_pairs_are_counted_only_once(self):
        """
        Tests that pairs of coordinates are counted only once.
        """
        # Arrange
        coords = [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
        expected = [((0, 4), (1, 9)), ((0, 4), (2, 0)), ((1, 9), (2, 0)), ((0, 4), (5, 8)),
                    ((1, 9), (5, 8)), ((2, 0), (5, 8)), ((0, 4), (6, 1)), ((1, 9), (6, 1)),
                    ((2, 0), (6, 1)), ((5, 8), (6, 1)), ((0, 4), (7, 12)), ((1, 9), (7, 12)),
                    ((2, 0), (7, 12)), ((5, 8), (7, 12)), ((6, 1), (7, 12)), ((0, 4), (10, 9)),
                    ((1, 9), (10, 9)), ((2, 0), (10, 9)), ((5, 8), (10, 9)), ((6, 1), (10, 9)),
                    ((7, 12), (10, 9)), ((0, 4), (11, 0)), ((1, 9), (11, 0)), ((2, 0), (11, 0)),
                    ((5, 8), (11, 0)), ((6, 1), (11, 0)), ((7, 12), (11, 0)), ((10, 9), (11, 0)),
                    ((0, 4), (11, 5)), ((1, 9), (11, 5)), ((2, 0), (11, 5)), ((5, 8), (11, 5)),
                    ((6, 1), (11, 5)), ((7, 12), (11, 5)), ((10, 9), (11, 5)), ((11, 0), (11, 5))]

        # Act
        actual = main.get_pairs(coords)

        # Assert
        self.assertListEqual(sorted(actual), sorted(expected))


class TestManhattanDistance(unittest.TestCase):
    """
    Class for testing the function that calculates the Manhattan distance between two points.
    """

    def test_calculations_are_correct(self):
        """
        Tests that the calculations are correct.
        """
        # Arrange
        coords = [
            ((6, 1), (11, 5)),  # galaxies 5 and 9
            ((0, 4), (10, 9)),  # galaxies 1 and 7
            ((2, 0), (7, 12)),  # galaxies 3 and 6
            ((11, 0), (11, 5)),  # galaxies 8 and 9
        ]
        expected = [9, 15, 17, 5]

        # Act
        actual = [main.manhattan_distance(p1, p2) for p1, p2 in coords]

        # Assert
        self.assertListEqual(actual, expected)


class TestPart1(unittest.TestCase):
    """
    Class for testing the function that solves part 1.
    """

    def test_outputs_correct_sum_distances_for_sample(self):
        """
        Tests that the function correctly finds the total sum of distances for the sample.
        """
        # Arrange
        filename = './aoc_2023/day11/sample.txt'
        expected = 374

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)

    def test_outputs_correct_sum_distances_for_input(self):
        """
        Tests that the function correctly finds the total sum of distances for the input.
        """
        # Arrange
        filename = './aoc_2023/day11/input.txt'
        expected = 9686930

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)
