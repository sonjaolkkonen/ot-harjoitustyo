import sys
sys.path.insert(0, '/home/olkkonso/ot-harjoitustyo/src')
import pygame
from sudoku import Sudoku
from game_loop import GameLoop

pygame.init()

screen = pygame.display.set_mode((550, 550))
pygame.display.set_caption("Aloitusvalikko")
main_font = pygame.font.SysFont('Arial', 30)

class Button:
    def __init__(self, image, x_pos, y_pos, content):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.content = content
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text = main_font.render(self.content, True, (255,255,255))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def new_game_button_is_pressed(self, position):
        from ui.ui import Ui
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Ui.choose_level(self)
    
    def statistics_button_is_pressed(self, position):
        from ui.ui import Ui
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Ui.statistics_screen(self)

    def menu_button_is_pressed(self, position):
        from ui.ui import Ui
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Ui()

    def easy_button_is_pressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Sudoku("easy")

    def medium_button_is_pressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Sudoku("medium")

    def hard_button_is_pressed(self, position):
        from ui.ui import Ui
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            Sudoku("hard")

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.content, True, (0,0,0))
        else:
            self.text = main_font.render(self.content, True, (255,255,255))



