import sys
import pygame
from button import Button


class Ui:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Aloitusvalikko")
        self.font = pygame.font.SysFont('Arial', 30)

        self.menu()

    def choose_level(self):
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Vaikeustaso")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:
            self.screen.fill((250, 250, 250))
            statistics_screen_text = self.font.render(
                "Valitse vaikeustaso", True, (0, 0, 0))
            statistics_screen_text_rect = statistics_screen_text.get_rect(
                center=(275, 100))
            self.screen.blit(statistics_screen_text,
                             statistics_screen_text_rect)

            button_image = pygame.image.load("src/button.png")
            button_image = pygame.transform.scale(button_image, (250, 100))
            easy_button = Button(button_image, 275, 200, "Helppo")
            medium_button = Button(button_image, 275, 300, "Keskivaikea")
            hard_button = Button(button_image, 275, 400, "Vaikea")

            for button in [easy_button, medium_button, hard_button]:
                button.update()
                button.change_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    easy_button.easy_button_is_pressed(pygame.mouse.get_pos())
                    medium_button.medium_button_is_pressed(
                        pygame.mouse.get_pos())
                    hard_button.hard_button_is_pressed(pygame.mouse.get_pos())

            pygame.display.update()

    def menu(self):
        button_image = pygame.image.load("src/button.png")
        button_image = pygame.transform.scale(button_image, (250, 100))
        new_game_button = Button(button_image, 275, 200, "Aloita uusi peli")
        statistics_button = Button(button_image, 275, 300, "Pelitilastot")

        while True:
            self.screen.fill((250, 250, 250))

            for button in [new_game_button, statistics_button]:
                button.update()
                button.change_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_game_button.new_game_button_is_pressed(
                        pygame.mouse.get_pos())
                    statistics_button.statistics_button_is_pressed(
                        pygame.mouse.get_pos())

            pygame.display.update()

    def end_screen(self):
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Pelitilastot")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:
            self.screen.fill((250, 250, 250))
            end_screen_text = self.font.render(
                "Peli läpi, onneksi olkoon!", True, (0, 0, 0))
            end_screen_text_rect = end_screen_text.get_rect(center=(275, 100))
            self.screen.blit(end_screen_text, end_screen_text_rect)

            button_image = pygame.image.load("src/button.png")
            button_image = pygame.transform.scale(button_image, (250, 100))
            new_game_button = Button(
                button_image, 275, 200, "Aloita uusi peli")
            menu_button = Button(button_image, 275, 300, "Palaa alkuun")

            for button in [new_game_button, menu_button]:
                button.update()
                button.change_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_game_button.new_game_button_is_pressed(
                        pygame.mouse.get_pos())
                    menu_button.menu_button_is_pressed(pygame.mouse.get_pos())

            pygame.display.update()

    def statistics_screen(self):
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Pelitilastot")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:

            self.screen.fill((250, 250, 250))
            statistics_screen_text = self.font.render(
                "Tähän tulee pelitilastot-näkymä", True, (0, 0, 0))
            statistics_screen_text_rect = statistics_screen_text.get_rect(
                center=(275, 100))
            self.screen.blit(statistics_screen_text,
                             statistics_screen_text_rect)

            button_image = pygame.image.load("src/button.png")
            button_image = pygame.transform.scale(button_image, (250, 100))
            menu_button = Button(button_image, 275, 200, "Palaa alkuun")

            menu_button.update()
            menu_button.change_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_button.menu_button_is_pressed(pygame.mouse.get_pos())

            pygame.display.update()


if __name__ == "__main__":
    Ui()
