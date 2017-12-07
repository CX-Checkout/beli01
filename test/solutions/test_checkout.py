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
        print('FINAL TEST 1')
        self.assertEqual(checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'), 1602)

    def test_checkout_final_test_2(self):
        self.assertEqual(checkout('LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH'), 1602)


if __name__ == '__main__':
    unittest.main()

{'A': {'count': 2, 'price': 100},
 'B': {'count': 1, 'price': 30},
 'C': {'count': 2, 'price': 40},
 'D': {'count': 2, 'price': 30},
 'E': {'count': 2, 'price': 80},
 'F': {'count': 2, 'price': 20},
 'G': {'count': 2, 'price': 40},
 'H': {'count': 2, 'price': 20},
 'I': {'count': 2, 'price': 70},
 'J': {'count': 2, 'price': 120},
 'K': {'count': 2, 'price': 120},
 'L': {'count': 2, 'price': 180},
 'M': {'count': 2, 'price': 30},
 'MIX_STXYZ': {'count': 3, 'price': 45},
 'N': {'count': 2, 'price': 80},
 'O': {'count': 2, 'price': 20},
 'P': {'count': 2, 'price': 100},
 'Q': {'count': 2, 'price': 60},
 'R': {'count': 2, 'price': 100},
 'S': {'count': 0, 'price': 0},
 'T': {'count': 0, 'price': 0},
 'U': {'count': 2, 'price': 80},
 'V': {'count': 2, 'price': 90},
 'W': {'count': 2, 'price': 40},
 'X': {'count': 1, 'price': 17},
 'Y': {'count': 0, 'price': 0},
 'Z': {'count': 0, 'price': 0}

+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+