import unittest
from services.game_loop import GameLoop

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.grid_complete = [[4, 3, 5, 9, 1, 6, 7, 2, 8], [1, 7, 6, 3, 2, 8, 4, 9, 5], [8, 2, 9, 5, 4, 7, 1, 3, 6], [5, 9, 4, 2, 8, 3, 6, 1, 7], [2, 1, 7, 4, 6, 9, 5, 8, 3], [3, 6, 8, 1, 7, 5, 2, 4, 9], [9, 8, 1, 7, 5, 2, 3, 6, 4], [6, 5, 2, 8, 3, 4, 9, 7, 1], [7, 4, 3, 6, 9, 1, 8, 5, 2]]
        self.grid_incomplete = [[0, 0, 5, 9, 1, 6, 7, 2, 8], [1, 7, 6, 3, 2, 8, 4, 9, 5], [8, 2, 9, 5, 4, 7, 1, 3, 6], [5, 9, 4, 2, 8, 3, 6, 1, 7], [2, 1, 7, 4, 6, 9, 5, 8, 3], [3, 6, 8, 1, 7, 5, 2, 4, 9], [9, 8, 1, 7, 5, 2, 3, 6, 4], [6, 5, 2, 8, 3, 4, 9, 7, 1], [7, 4, 3, 6, 9, 1, 8, 5, 2]]

    def test_count_scores(self):
        scores = GameLoop.count_scores(self, 90)
        
        self.assertEqual(scores, 130)

    def test_number_already_in_row(self):
        number_in_row = GameLoop.number_already_in_row(self.grid_complete, 0, 4)
        
        self.assertTrue(number_in_row)

        number_in_row = GameLoop.number_already_in_row(self.grid_incomplete, 0, 4)

        self.assertFalse(number_in_row)

    def test_number_already_in_col(self):
        number_in_col = GameLoop.number_already_in_col(self.grid_complete, 0, 4)

        self.assertTrue(number_in_col)

        number_in_col = GameLoop.number_already_in_col(self.grid_incomplete, 0, 4)

        self.assertFalse(number_in_col)

    def test_number_already_in_subgrid(self):
        number_in_subgrid = GameLoop.number_already_in_subgrid(self.grid_complete, 0, 0, 4)

        self.assertTrue(number_in_subgrid)

        number_in_subgrid = GameLoop.number_already_in_subgrid(self.grid_incomplete, 0, 0, 4)

        self.assertFalse(number_in_subgrid)

    def test_get_filled_cells(self):
        filled_cells = GameLoop.get_filled_cells(self.grid_complete)

        self.assertEqual(len(filled_cells), 81)


    def test_find_empty_cells(self):
        empty_cells = GameLoop.find_empty_cell(self.grid_incomplete)

        self.assertEqual(empty_cells, (0,0))

        empty_cells = GameLoop.find_empty_cell(self.grid_complete)

        self.assertEqual(empty_cells, None)

    def test_valid_location(self):
        self.number_already_in_row = GameLoop.number_already_in_row(self.grid_complete, 0, 4)

        valid_location = GameLoop.valid_location(self.grid_complete, 0, 0, 4)

        self.assertFalse(valid_location)
