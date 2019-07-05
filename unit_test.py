#\mikeProgs\Treehouse> python -m unittest unit_test.py
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.000s
#
#OK
import unittest

import moves

class MoveTests(unittest.TestCase):
    def setUp(self):
        # use setUp to avoid making a bunch of instantiations .. see commented code
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_five_plus_five(self):
        assert 5+ 5 == 10
        
    def test_one_plus_one(self):
        assert not 1 + 1 ==3
        
    def test_equal(self):
        #rock1 = moves.Rock()
        #rock2 = moves.Rock()
        #self.assertEqual(rock1, rock2)
        self.assertEqual(self.rock, moves.Rock())
        
    def test_not_equal(self):
        #rock = moves.Rock()
        #paper = moves.Paper()
        #self.assertNotEqual(rock, paper)
        self.assertNotEqual(self.rock, self.paper)
    
    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)
        
    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper, self.scissors)
        
        
if __name__ == '__main__':
    unittest.main()
    
        
