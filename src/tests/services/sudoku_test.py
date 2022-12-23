import unittest
from services.game_loop import GameLoop


class TestSudoku(unittest.TestCase):
    def setUp(self):
        position = None
        screen = None
        font = None
        number = None
        grid = None

        self.game_loop = GameLoop(position, screen, font, number, grid, level="easy")

    def test_grid_has_nine_3x3_grids(self):
        self.game_loop.new_game()
        self.assertEqual(len(self.grid), 9)
