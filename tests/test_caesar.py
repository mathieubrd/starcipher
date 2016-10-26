import unittest
from starcipher.caesar import Caesar
from starcipher.dictionnary import Dictionnary

class TestCaesar(unittest.TestCase):
    def setUp(self):
        self.dict = Dictionnary('tests/en.dict')

    def test_encrypt(self):
        self.assertEqual(
            Caesar.encrypt(9, 'TO BE OR NOT TO BE, THAT\'S THE QUESTION.'),
            'CX KN XA WXC CX KN, CQJC\'B CQN ZDNBCRXW.'
        )

    def test_decrypt(self):
        self.assertEqual(
            Caesar.decrypt(9, 'CX KN XA WXC CX KN, CQJC\'B CQN ZDNBCRXW.'),
            'TO BE OR NOT TO BE, THAT\'S THE QUESTION.'
        )

    def test_brute_force(self):
        self.assertEqual(
            Caesar.brute_force('DRSC SC K COMBOD WOCCKQO, XYLYNI GSVV NSCMYFOB SD.', self.dict),
            'THIS IS A SECRET MESSAGE, NOBODY WILL DISCOVER IT.'
        )
