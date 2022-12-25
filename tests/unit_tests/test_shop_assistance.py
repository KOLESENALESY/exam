import unittest

from prod.model.entity import *
from prod.model.logic import *


class TestShopAssistance(unittest.TestCase):

    def test_calculate_total_price_basic(self):
        gift = Gift()
        gift.add(Sweet("", 1.5))
        gift.add(Sweet("", 2.5))
        gift.add(Sweet("", 3.5))
        expected = 7.5

        actual = ShopAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)

    #...
    def test_calculate_total_price_with_incorrect_data(self):
        expected = -1
        actual = ShopAssistance.calculate_total_price(10)

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_empty_gift(self):
        expected = 0
        actual = ShopAssistance.calculate_total_price(Gift())

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_sweet(self):
        gift = Gift()
        sweet = Sweet(10)
        gift.add(sweet)
        expected = sweet.price

        actual = ShopAssistance.calculate_total_price(gift)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
