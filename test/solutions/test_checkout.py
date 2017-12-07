import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout_special_offer_2_for_A_products(self):
        self.assertEqual(checkout('AAAAA'), 200)


if __name__ == '__main__':
    unittest.main()
