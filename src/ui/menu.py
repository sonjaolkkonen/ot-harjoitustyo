import sys
import pygame
from button import Button

class Menu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Aloitusvalikko")
        self.font = pygame.font.SysFont('Arial', 30)

        self.loop()

    def loop(self):
        button_image = pygame.image.load("src/button.png")
        button_image = pygame.transform.scale(button_image, (250,100))
        new_game_button = Button(button_image, 275, 200, "Aloita uusi peli")
        statistics_button =Button(button_image, 275, 300, "Pelitilastot")

        while True:
            self.screen.fill((250,250,250))
            
            for button in [new_game_button, statistics_button]:
                button.update()
                button.change_color(pygame.mouse.get_pos())
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_game_button.new_game_button_is_pressed(pygame.mouse.get_pos())
                    statistics_button.statistics_button_is_pressed(pygame.mouse.get_pos())
 
               
            pygame.display.update()

if __name__ == "__main__":
    Menu()