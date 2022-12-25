import unittest
from prod.model.entity import *


class TestProduct(unittest.TestCase):
    def test_setter_positive(self):
        sweet = Sweet()
        sweet.price = 10

        expected = 10

        actual = sweet.price

        self.assertEqual(expected, actual)

    def test_setter_without_price(self):
        sweet = Sweet()

        expected = 0

        actual = sweet.price

        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        sweet = Sweet()

        self.assertRaises(ValueError, sweet.price, 10)


if __name__ == "__main__":
    unittest.main()
