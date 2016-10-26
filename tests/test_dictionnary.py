import unittest
from starcipher.dictionnary import Dictionnary

class TestDictionnary(unittest.TestCase):

    def setUp(self):
        self.dictionnary = Dictionnary('tests/en.dict')

    def test_contains(self):
        self.assertEqual(self.dictionnary.contains('what'), True)
        self.assertEqual(self.dictionnary.contains('proutcaca'), False)
        self.assertEqual(self.dictionnary.contains('question'), True)
