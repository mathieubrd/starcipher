import unittest
from starcipher.vigenere import Vigenere

class TestVigenere(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(
            Vigenere.encrypt('KEY', 'BONJOUR'),
            'LSLTSSB'
        )
        self.assertEqual(
            Vigenere.encrypt('LEMON', 'ATTACK AT DAWN'),
            'LXFOPV EF RNHR'
        )

    def test_decrypt(self):
        self.assertEqual(
            Vigenere.decrypt('KEY', 'LSLTSSB'),
            'BONJOUR'
        )
        self.assertEqual(
            Vigenere.decrypt('LEMON', 'LXFOPV EF RNHR'),
            'ATTACK AT DAWN'
        )
