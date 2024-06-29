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
        self.assertEqual(actual, expected)

    def test_type_five_of_a_kind(self):
        """
        Tests whether recognizing five of a kind works.
        """
        # Arrange
        hand = 'AAAAA'
        expected = main.CardType.FIVE_OF_A_KIND

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_four_of_a_kind(self):
        """
        Tests whether recognizing four of a kind works.
        """
        # Arrange
        hand = 'AA8AA'
        expected = main.CardType.FOUR_OF_A_KIND

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_full_house(self):
        """
        Tests whether recognizing full house works.
        """
        # Arrange
        hand = '23332'
        expected = main.CardType.FULL_HOUSE

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_three_of_kind(self):
        """
        Tests whether recognizing three of a kind works.
        """
        # Arrange
        hand = 'TTT98'
        expected = main.CardType.THREE_OF_A_KIND

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_two_pair(self):
        """
        Tests whether recognizing two pair works.
        """
        # Arrange
        hand = '23432'
        expected = main.CardType.TWO_PAIR

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_one_pair(self):
        """
        Tests whether recognizing one pair works.
        """
        # Arrange
        hand = 'A23A4'
        expected = main.CardType.ONE_PAIR

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_high_card(self):
        """
        Tests whether recognizing high card works.
        """
        # Arrange
        hand = '23456'
        expected = main.CardType.HIGH_CARD

        # Act
        actual = main.type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_compare_equal_types_four_of_a_kind(self):
        """
        Tests whether comparing equal types works for four of a kind.
        """
        # Arrange
        hand1 = '33332'
        hand2 = '2AAAA'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(actual, expected)

    def test_comparator_equal_inputs(self):
        """
        Tests that comparing cards returns 0 when the inputs are equal.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = '32T3K'
        expected = 0

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v1(self):
        """
        Tests that comparing cards works - variant 1.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v2(self):
        """
        Tests that comparing cards works - variant 2.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v3(self):
        """
        Tests that comparing cards works - variant 3.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = 'KTJJT'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v4(self):
        """
        Tests that comparing cards works - variant 4.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v5(self):
        """
        Tests that comparing cards works - variant 5.
        """
        # Arrange
        hand1 = 'T55J5'
        hand2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v6(self):
        """
        Tests that comparing cards works - variant 6.
        """
        # Arrange
        hand1 = 'T55J5'
        hand2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v7(self):
        """
        Tests that comparing cards works - variant 7.
        """
        # Arrange
        hand1 = 'T55J5'
        hand2 = 'KTJJT'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v8(self):
        """
        Tests that comparing cards works - variant 8.
        """
        # Arrange
        hand1 = 'T55J5'
        hand2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v9(self):
        """
        Tests that comparing cards works - variant 9.
        """
        # Arrange
        hand1 = 'KK677'
        hand2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v10(self):
        """
        Tests that comparing cards works - variant 10.
        """
        # Arrange
        hand1 = 'KK677'
        hand2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v11(self):
        """
        Tests that comparing cards works - variant 11.
        """
        # Arrange
        hand1 = 'KK677'
        hand2 = 'KTJJT'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v12(self):
        """
        Tests that comparing cards works - variant 12.
        """
        # Arrange
        hand1 = 'KK677'
        hand2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v13(self):
        """
        Tests that comparing cards works - variant 13.
        """
        # Arrange
        hand1 = 'KTJJT'
        hand2 = '32T3K'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v14(self):
        """
        Tests that comparing cards works - variant 14.
        """
        # Arrange
        hand1 = 'KTJJT'
        hand2 = 'T55J5'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v15(self):
        """
        Tests that comparing cards works - variant 15.
        """
        # Arrange
        hand1 = 'KTJJT'
        hand2 = 'KK677'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v16(self):
        """
        Tests that comparing cards works - variant 16.
        """
        # Arrange
        hand1 = 'KTJJT'
        hand2 = 'QQQJA'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v17(self):
        """
        Tests that comparing cards works - variant 17.
        """
        # Arrange
        hand1 = 'QQQJA'
        hand2 = '32T3K'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v18(self):
        """
        Tests that comparing cards works - variant 18.
        """
        # Arrange
        hand1 = 'QQQJA'
        hand2 = 'T55J5'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v19(self):
        """
        Tests that comparing cards works - variant 19.
        """
        # Arrange
        hand1 = 'QQQJA'
        hand2 = 'KK677'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

    def test_comparator_v20(self):
        """
        Tests that comparing cards works - variant 20.
        """
        # Arrange
        hand1 = 'QQQJA'
        hand2 = 'KTJJT'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(expected, actual)

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
        self.assertListEqual(actual, expected)
