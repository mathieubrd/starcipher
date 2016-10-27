import unittest
from starcipher.dictionnary import Dictionnary
from starcipher.affine import Affine

class TestAffine(unittest.TestCase):

    def setUp(self):
        self._dictionnary = Dictionnary('tests/en.dict')

    def test_xgcd(self):
        self.assertEqual(Affine.xgcd(7, 3), (1, 1, -2))
        self.assertEqual(Affine.xgcd(14812, 1482), (2, 185, -1849))

    def test_mod_inv(self):
        self.assertEqual(Affine.mod_inv(7841, 41), 37)
        self.assertNotEqual(Affine.mod_inv(451, 78), 1)

    def test_is_prime(self):
        self.assertEqual(Affine.is_prime(1), True)
        self.assertEqual(Affine.is_prime(2), True)
        self.assertEqual(Affine.is_prime(3), True)
        self.assertEqual(Affine.is_prime(4), False)
        self.assertEqual(Affine.is_prime(5), True)
        self.assertEqual(Affine.is_prime(7), True)
        self.assertEqual(Affine.is_prime(8), False)

    def test_inv_mod(self):
        self.assertEqual(Affine.mod_inv(3, 26), 9)

    def test_encrypt(self):
        self.assertEqual(
            Affine.encrypt(3, 12, 'HEY, THIS IS THE AFFINE CIPHER!'),
            'HYG, RHKO KO RHY MBBKZY SKFHYL!'
        )

    def test_decrypt(self):
        self.assertEqual(
            Affine.decrypt(3, 12, 'HYG, RHKO KO RHY MBBKZY SKFHYL!'),
            'HEY, THIS IS THE AFFINE CIPHER!'
        )

    def test_brute_force(self):
        self.assertEqual(
            Affine.brute_force('GWZD ZD B GNDG RQ GWN BQQZON HZUWNA. Z WRUN ZG PZII EN HABHFNK!', self._dictionnary),
            'THIS IS A TEST OF THE AFFINE CIPHER. I HOPE IT WILL BE CRACKED!'
        )
