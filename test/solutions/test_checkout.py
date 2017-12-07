import unittest

from lib.solutions.checkout import checkout, mix_and_match_filter


class TestMixAndMatchFilter(unittest.TestCase):

    def test_mix_and_match(self):
        self.assertEqual(mix_and_match_filter({'S': {'count': 4, 'price': 0}}),
                                              {'S': {'count': 1, 'price': 0},
                                               'T': {'count': 0, 'price': 0},
                                               'X': {'count': 0, 'price': 0},
                                               'Y': {'count': 0, 'price': 0},
                                               'Z': {'count': 0, 'price': 0},
                                               'MIX_STXYZ': {'count': 1, 'price': 0}})


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

    def test_checkout_inter_product_mix_not_applies_for_2_products(self):
        self.assertEqual(checkout('XY'), 37)

    def test_checkout_inter_product_mix_applies_for_3_products_of_3_different_types(self):
        self.assertEqual(checkout('XYZ'), 45)

    def test_checkout_inter_product_mix_applies_for_3_products_but_only_2_different_types(self):
        self.assertEqual(checkout('XXZ'), 45)

    def test_checkout_inter_product_mix_applies_for_3_products_but_only_1_type(self):
        self.assertEqual(checkout('XXX'), 45)

    def test_checkout_inter_product_for_KK_products(self):
        self.assertEqual(checkout('KK'), 120)

    def test_checkout_inter_product_for_SSSZ_products(self):
        self.assertEqual(checkout('SSSZ'), 65)

    def test_checkout_inter_product_for_ZZZS_products(self):
        self.assertEqual(checkout('ZZZS'), 65)

    def test_checkout_inter_product_for_STXS_products(self):
        self.assertEqual(checkout('STXS'), 62)

    def test_checkout_final_test_1(self):
        self.assertEqual(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'), 1602)

    def test_checkout_final_test_2(self):
        self.assertEqual(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'), 1602)


if __name__ == '__main__':
    unittest.main()
