import unittest

from aoc_2023.day07 import main


class TestDay07(unittest.TestCase):

    def test_parsing_input(self):
        """
        Tests that parsing the input returns a dictionary from card to its bid.
        """
        # Arrange
        filename = 'aoc_2023/day07/sample.txt'
        expected = {
            '32T3K': 765,
            'T55J5': 684,
            'KK677': 28,
            'KTJJT': 220,
            'QQQJA': 483,
        }

        # Act
        actual = main.parse_input(filename)

        # Assert
        self.assertEqual(
            actual, expected, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_equal_inputs(self):
        """
        Tests that comparing cards returns 0 when the inputs are equal.
        """
        # Arrange
        card1 = '32T3K'
        card2 = '32T3K'
        expected = 0

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v1(self):
        """
        Tests that comparing cards works - variant 1.
        """
        # Arrange
        card1 = '32T3K'
        card2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v2(self):
        """
        Tests that comparing cards works - variant 2.
        """
        # Arrange
        card1 = '32T3K'
        card2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v3(self):
        """
        Tests that comparing cards works - variant 3.
        """
        # Arrange
        card1 = '32T3K'
        card2 = 'KTJJT'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v4(self):
        """
        Tests that comparing cards works - variant 4.
        """
        # Arrange
        card1 = '32T3K'
        card2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v5(self):
        """
        Tests that comparing cards works - variant 5.
        """
        # Arrange
        card1 = 'T55J5'
        card2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v6(self):
        """
        Tests that comparing cards works - variant 6.
        """
        # Arrange
        card1 = 'T55J5'
        card2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v7(self):
        """
        Tests that comparing cards works - variant 7.
        """
        # Arrange
        card1 = 'T55J5'
        card2 = 'KTJJT'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v8(self):
        """
        Tests that comparing cards works - variant 8.
        """
        # Arrange
        card1 = 'T55J5'
        card2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v9(self):
        """
        Tests that comparing cards works - variant 9.
        """
        # Arrange
        card1 = 'KK677'
        card2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v10(self):
        """
        Tests that comparing cards works - variant 10.
        """
        # Arrange
        card1 = 'KK677'
        card2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v11(self):
        """
        Tests that comparing cards works - variant 11.
        """
        # Arrange
        card1 = 'KK677'
        card2 = 'KTJJT'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v12(self):
        """
        Tests that comparing cards works - variant 12.
        """
        # Arrange
        card1 = 'KK677'
        card2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v13(self):
        """
        Tests that comparing cards works - variant 13.
        """
        # Arrange
        card1 = 'KTJJT'
        card2 = '32T3K'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v14(self):
        """
        Tests that comparing cards works - variant 14.
        """
        # Arrange
        card1 = 'KTJJT'
        card2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v15(self):
        """
        Tests that comparing cards works - variant 15.
        """
        # Arrange
        card1 = 'KTJJT'
        card2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v16(self):
        """
        Tests that comparing cards works - variant 16.
        """
        # Arrange
        card1 = 'KTJJT'
        card2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v17(self):
        """
        Tests that comparing cards works - variant 17.
        """
        # Arrange
        card1 = 'QQQJA'
        card2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v18(self):
        """
        Tests that comparing cards works - variant 18.
        """
        # Arrange
        card1 = 'QQQJA'
        card2 = 'T55J5'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v19(self):
        """
        Tests that comparing cards works - variant 19.
        """
        # Arrange
        card1 = 'QQQJA'
        card2 = 'KK677'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_comparator_v20(self):
        """
        Tests that comparing cards works - variant 20.
        """
        # Arrange
        card1 = 'QQQJA'
        card2 = 'KTJJT'
        expected = -1

        # Act
        actual = main.compare(card1, card2)

        # Assert
        self.assertEqual(
            expected, actual, f'Expected to get {expected}, but got {actual}.'
        )

    def test_order_by_rank(self):
        """
        Tests that ordering by rank works.
        """
        # Arrange
        cards = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
        expected = ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']

        # Act
        actual = main.order_by_rank(cards)

        # Assert
        self.assertListEqual(
            actual, expected, f'Expected to get {expected}, but got {actual}.'
        )
