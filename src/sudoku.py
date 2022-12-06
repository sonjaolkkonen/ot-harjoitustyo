import pygame
from game_loop import GameLoop


class Sudoku:
    def __init__(self, level):

        pygame.init()

        self.screen = pygame.display.set_mode((800, 550))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('Arial', 30)
        self.number = None
        self.grid = None
        self.level = level

        screen = self.screen
        position = pygame.mouse.get_pos()
        font = self.font
        number = self.number
        grid = self.grid

        GameLoop(position, screen, font, number, grid, level)
