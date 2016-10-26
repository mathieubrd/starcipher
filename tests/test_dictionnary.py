import unittest
from starcipher.dictionnary import Dictionnary

class TestDictionnary(unittest.TestCase):

    def setUp(self):
        self.dictionnary = Dictionnary('tests/en.dict')

    def test_recognize(self):
        self.assertEqual(self.dictionnary.recognize('hello my name is'), 1)
        self.assertEqual(self.dictionnary.recognize('hello my name ekfkzf'), 0.75)
        self.assertEqual(self.dictionnary.recognize('zfkeof oekf psofp oekkofs e'), 0)
