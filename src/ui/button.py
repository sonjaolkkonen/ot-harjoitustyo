import pygame

pygame.init()

screen = pygame.display.set_mode((550, 550))
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
        self.number = None
        self.grid = None

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def is_pressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.content, True, (0,0,0))
        else:
            self.text = main_font.render(self.content, True, (255,255,255))



