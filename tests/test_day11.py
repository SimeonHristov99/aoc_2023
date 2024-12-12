import unittest

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


class TestExpand(unittest.TestCase):
    """
    Class for testing the function that expands the universe.
    """

    def test_expand_sample(self):
        """
        Tests that the function expands the universe in the sample file correctly.
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
        expected_after_expansion = [
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

        # Act
        actual_after_expansion = main.expand(universe)

        # Assert
        self.assertListEqual(actual_after_expansion, expected_after_expansion)


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

    def test_outputs_correct_number_of_galaxies_for_sample(self):
        """
        Tests that the function correctly finds the number of galaxies in the sample.
        """
        # Arrange
        filename = './aoc_2023/day11/sample.txt'
        expected = 9

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)

    def test_outputs_correct_number_of_galaxies_for_input(self):
        """
        Tests that the function correctly finds the number of galaxies in the input.
        """
        # Arrange
        filename = './aoc_2023/day11/input.txt'
        expected = 439

        # Act
        actual = main.part1(filename)

        # Assert
        self.assertEqual(actual, expected)
