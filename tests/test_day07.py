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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

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
        actual = main.card_type(hand)

        # Assert
        self.assertEqual(actual, expected)

    def test_full_house_stronger_than_three_of_a_kind(self):
        """
        Tests that comparing unequal types favors the stronger type.
        """
        # Arrange
        hand1 = '23332'
        hand2 = 'TTT98'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(actual, expected)

    def test_three_of_a_kind_weaker_than_full_house(self):
        """
        Tests that comparing unequal types favors the stronger type.
        """
        # Arrange
        hand1 = 'TTT98'
        hand2 = '23332'
        expected = -1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(actual, expected)

    def test_compare_equal_types_four_of_a_kind(self):
        """
        Tests whether comparing equal types works for four of a kind.
        """
        # Arrange
        hand1 = '33332'
        hand2 = '2AAAA'
        expected = 1

        # Act
        actual = main.compare(hand1, hand2)

        # Assert
        self.assertEqual(actual, expected)

    def test_comparator_raises_on_equal_inputs(self):
        """
        Tests that comparing identical hands raises a `NotImplementedError` since this cannot happen.
        """
        # Arrange
        hand1 = '32T3K'
        hand2 = '32T3K'

        # Act & Assert
        self.assertRaises(NotImplementedError, main.compare, hand1, hand2)

    def test_comparator(self):
        """
        Tests that comparing cards works.
        """
        # Arrange
        trials = [
            ('32T3K', 'T55J5', -1),
            ('32T3K', 'KK677', -1),
            ('32T3K', 'KTJJT', -1),
            ('32T3K', 'QQQJA', -1),
            ('T55J5', '32T3K', 1),
            ('T55J5', 'KK677', 1),
            ('T55J5', 'KTJJT', 1),
            ('T55J5', 'QQQJA', -1),
            ('KK677', '32T3K', 1),
            ('KK677', 'T55J5', -1),
            ('KK677', 'KTJJT', 1),
            ('KK677', 'QQQJA', -1),
            ('KTJJT', '32T3K', 1),
            ('KTJJT', 'T55J5', -1),
            ('KTJJT', 'KK677', -1),
            ('KTJJT', 'QQQJA', -1),
            ('QQQJA', '32T3K', 1),
            ('QQQJA', 'T55J5', 1),
            ('QQQJA', 'KK677', 1),
            ('QQQJA', 'KTJJT', 1),
        ]

        # Act & Assert
        for hand1, hand2, expected in trials:
            self.assertEqual(
                main.compare(hand1, hand2), expected,
                f'Expected {expected} for {hand1=} and {hand2=}.'
            )

    def test_order_by_rank_no_joker(self):
        """
        Tests that ordering by rank works when `J` is not treated as a joker card.
        """
        # Arrange
        cards = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
        expected = ['32T3K', 'KTJJT', 'KK677', 'T55J5', 'QQQJA']

        # Act
        actual = main.order_by_rank(cards)

        # Assert
        self.assertListEqual(actual, expected)

    def test_type_with_joker_two_pair_four_of_a_kind_when_two_jokers(self):
        """
        Tests that when `J` is treated as a joker card two pair becomes four of a kind when there are two `J`s.
        """
        # Arrange
        hand = 'KTJJT'
        expected = main.CardType.FOUR_OF_A_KIND

        # Act
        actual = main.card_type(hand, joker=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_with_joker_two_pair_three_of_a_kind_one_joker(self):
        """
        Tests that when `J` is treated as a joker card two pair becomes three of a kind when there is one `J`.
        """
        # Arrange
        hand = 'KKJTT'
        expected = main.CardType.THREE_OF_A_KIND

        # Act
        actual = main.card_type(hand, joker=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_with_joker_three_of_a_kind_full_house_when_one_joker(self):
        """
        Tests that when `J` is treated as a joker card three of a kind becomes full house when there is one `J`.
        """
        # Arrange
        hand = 'KTJTT'
        expected = main.CardType.FOUR_OF_A_KIND

        # Act
        actual = main.card_type(hand, joker=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_with_joker_one_pair_three_of_a_kind(self):
        """
        Tests that when `J` is treated as a joker card one pair becomes three of a kind where there is one `J`.
        """
        # Arrange
        hand = 'A2JA4'
        expected = main.CardType.THREE_OF_A_KIND

        # Act
        actual = main.card_type(hand, joker=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_with_joker_high_card_becomes_one_pair(self):
        """
        Tests that when `J` is treated as a joker card high card becomes one pair when there is one `J`.
        """
        # Arrange
        hand = '23J56'
        expected = main.CardType.ONE_PAIR

        # Act
        actual = main.card_type(hand, joker=True)

        # Assert
        self.assertEqual(actual, expected)

    def test_type_with_joker_full_house_becomes_five_of_a_kind(self):
        """
        Tests that when `J` is treated as a joker card, full house becomes five of a kind.
        """
        # Arrange
        hand1 = 'J333J'
        hand2 = '3JJJ3'
        expected = main.CardType.FIVE_OF_A_KIND

        # Act
        actual1 = main.card_type(hand1, joker=True)
        actual2 = main.card_type(hand2, joker=True)

        # Assert
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)

    def test_type_without_joker_full_house_does_not_change(self):
        """
        Tests that when `J` is not treated as a joker card, full house does not change.
        """
        # Arrange
        hand1 = 'J333J'
        hand2 = '3JJJ3'
        expected = main.CardType.FULL_HOUSE

        # Act
        actual1 = main.card_type(hand1)
        actual2 = main.card_type(hand2)

        # Assert
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)

    def test_type_with_joker_four_of_a_kind_becomes_five_of_a_kind(self):
        """
        Tests that when `J` is treated as a joker card, four of a kind becomes five of a kind.
        """
        # Arrange
        hand1 = 'AAJAA'
        hand2 = 'JJAJJ'
        expected = main.CardType.FIVE_OF_A_KIND

        # Act
        actual1 = main.card_type(hand1, joker=True)
        actual2 = main.card_type(hand2, joker=True)

        # Assert
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)

    def test_type_without_joker_four_of_a_kind_does_not_change(self):
        """
        Tests that when `J` is not treated as a joker card, four of a kind does not change.
        """
        # Arrange
        hand1 = 'AAJAA'
        hand2 = 'JJAJJ'
        expected = main.CardType.FOUR_OF_A_KIND

        # Act
        actual1 = main.card_type(hand1)
        actual2 = main.card_type(hand2)

        # Assert
        self.assertEqual(actual1, expected)
        self.assertEqual(actual2, expected)

    def test_comparator_with_joker(self):
        """
        Tests that comparing cards works when `J` is treated as a joker card.
        """
        # Arrange
        trials = [
            ('32T3K', 'T55J5', -1),
            ('32T3K', 'KK677', -1),
            ('32T3K', 'KTJJT', -1),
            ('32T3K', 'QQQJA', -1),
            ('T55J5', '32T3K', 1),
            ('T55J5', 'KK677', 1),
            ('T55J5', 'KTJJT', -1),
            ('T55J5', 'QQQJA', -1),
            ('KK677', '32T3K', 1),
            ('KK677', 'T55J5', -1),
            ('KK677', 'KTJJT', -1),
            ('KK677', 'QQQJA', -1),
            ('KTJJT', '32T3K', 1),
            ('KTJJT', 'T55J5', 1),
            ('KTJJT', 'KK677', 1),
            ('KTJJT', 'QQQJA', 1),
            ('QQQJA', '32T3K', 1),
            ('QQQJA', 'T55J5', 1),
            ('QQQJA', 'KK677', 1),
            ('QQQJA', 'KTJJT', -1),
        ]

        # Act & Assert
        for hand1, hand2, expected in trials:
            self.assertEqual(
                main.compare(hand1, hand2, joker=True), expected,
                f'Expected {expected} for {hand1=} and {hand2=}.'
            )

    def test_order_by_rank_with_joker(self):
        """
        Tests that ordering by rank works when `J` is treated as a joker card.
        """
        # Arrange
        cards = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
        expected = ['32T3K', 'KK677', 'T55J5', 'QQQJA', 'KTJJT']

        # Act
        actual = main.order_by_rank(cards, joker=True)

        # Assert
        self.assertListEqual(actual, expected)
