import pygame
from game_loop import GameLoop


class Sudoku:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('Arial', 30)
        self.number = None
        self.grid = None

        self.draw_screen()
        self.draw_lines()


        screen = self.screen
        position = pygame.mouse.get_pos()
        font = self.font
        number = self.number
        grid = self.grid
        game_loop = GameLoop(position, screen, font, number, grid)
        game_loop.new_game()
        game_loop.handle_events()

    # drawing the screen
    def draw_screen(self):
        self.screen.fill((255, 250, 240))

    # drawing the grid & 9x9 boxes
    def draw_lines(self):

        for i in range(0, 10):
            # 9x9 boxes
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50+50*i, 50), (50+50*i, 500), 5)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50, 50+50*i), (500, 50+50*i), 5)

            # vertical lines
            pygame.draw.line(self.screen, (0, 0, 0),
                             (50+50*i, 50), (50+50*i, 500), 2)
            # horizontal lines
            pygame.draw.line(self.screen, (0, 0, 0),
                             (50, 50+50*i), (500, 50+50*i), 2)
        pygame.display.update()


if __name__ == "__main__":
    Sudoku()
