import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromos_simples(self):
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("anilina"))
        self.assertTrue(is_palindrome("menem"))
    def test_frases_palindromas(self):
        self.assertTrue(is_palindrome("La ruta natural"))
        self.assertTrue(is_palindrome("Amor a Roma"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
    def test_no_palindromos(self):
        self.assertFalse(is_palindrome("computadora"))
        self.assertFalse(is_palindrome("ingeniería"))
        self.assertFalse(is_palindrome("universidad nacional"))