import unittest
from services.game_loop import GameLoop

class TestSudoku(unittest.TestCase):
    def setUp(self):
        row = None
        col = None
        number = None
        self.valid_location = GameLoop.valid_location(self, [[5, 1, 4, 7, 8, 3, 2, 6, 9], [6, 7, 8, 9, 4, 2, 3, 1, 5], [3, 2, 9, 6, 1, 5, 8, 4, 7], [4, 8, 5, 2, 6, 7, 9, 3, 1], [7, 3, 2, 8, 9, 1, 4, 5, 6], [1, 9, 6, 3, 5, 4, 7, 2, 8], [2, 4, 1, 5, 7, 8, 6, 9, 3], [8, 6, 3, 1, 2, 9, 5, 7, 4], [9, 5, 7, 4, 3, 6, 1, 8, 2]], row, col, number)

    def test_test_solution(self):
        grid = [[5, 1, 4, 7, 8, 3, 2, 6, 9], [6, 7, 8, 9, 4, 2, 3, 1, 5], [3, 2, 9, 6, 1, 5, 8, 4, 7], [4, 8, 5, 2, 6, 7, 9, 3, 1], [7, 3, 2, 8, 9, 1, 4, 5, 6], [1, 9, 6, 3, 5, 4, 7, 2, 8], [2, 4, 1, 5, 7, 8, 6, 9, 3], [8, 6, 3, 1, 2, 9, 5, 7, 4], [9, 5, 7, 4, 3, 6, 1, 8, 2]]
        solution = GameLoop.test_solution(self, grid)
        self.assertTrue(solution)



