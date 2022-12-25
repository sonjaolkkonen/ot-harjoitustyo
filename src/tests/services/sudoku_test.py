import unittest
from services.game_loop import GameLoop

class TestSudoku(unittest.TestCase):
    def test_count_scores(self):
        scores = GameLoop.count_scores(self, 90)
        
        self.assertEqual(scores, 130)