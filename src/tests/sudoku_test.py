import unittest
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku()

    def test_grid_has_nine_3x3_grids(self):
        self.sudoku.new_game()
        self.assertEqual(len(self.grid), 9)
