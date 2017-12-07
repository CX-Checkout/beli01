import unittest

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):

    def test_checkout_special_offer_2_for_A_products(self):
        self.assertEqual(checkout('AAAAA'), 200)

    def test_checkout_special_offer_1_and_2_for_A_products(self):
        self.assertEqual(checkout('AAAAAAAA'), 330)

    def test_checkout_special_offer_1_and_2_and_remaining_for_A_products(self):
        self.assertEqual(checkout('AAAAAAAAA'), 380)

    def test_checkout_special_offer_for_B_products(self):
        self.assertEqual(checkout('BB'), 45)

    def test_checkout_special_offer_and_remaining_for_B_products(self):
        self.assertEqual(checkout('BBB'), 75)

    def test_checkout_inter_product_for_E_and_special_offer_for_B_products(self):
        self.assertEqual(checkout('BEE'), 80)

    def test_checkout_inter_product_for_E_and_special_offer_and_remaining_for_B_products(self):
        self.assertEqual(checkout('BBEE'), 110)

    def test_checkout_inter_product_for_F_products(self):
        self.assertEqual(checkout('FF'), 20)

    def test_checkout_inter_product_for_F_products(self):
        self.assertEqual(checkout('FFF'), 20)

    def test_checkout_inter_product_and_remaining_for_F_products(self):
        self.assertEqual(checkout('FFFF'), 30)


if __name__ == '__main__':
    unittest.main()
