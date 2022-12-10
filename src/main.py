import pygame

class Sudoku:
    def __init__(self):
        pass

    def play(self):
        from ui.ui import Ui    


        pygame.init()

        self.screen = pygame.display.set_mode((800, 550))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('Arial', 30)
        self.screen.fill((255, 250, 240))

        Ui()



if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.play()
