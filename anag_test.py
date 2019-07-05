import unittest

from string_fun import get_anagrams

class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn('house', get_anagrams('treehouse'))
        
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.get_anagrams('') 
        # pass
        
    def test_no_args(self):
        with self.assertRaises(ValueError):
            self.get_anagrams()