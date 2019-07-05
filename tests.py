import unittest

from string_fun import is_palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        self.assertTrue(is_palindrome('tacocat'))
        #pass
      
    def test_bad_palindrome(self):
        self.assertFalse(is_palindrome('hebahebaheba'))
        #pass
        
