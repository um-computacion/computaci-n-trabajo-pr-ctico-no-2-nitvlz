import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromos_simples(self):
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("anilina"))
        self.assertTrue(is_palindrome("menem"))
