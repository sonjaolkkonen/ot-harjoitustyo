import sys
import pygame
import os

from ui.textbox import TextBox
from ui.button import Button

dirname = os.path.dirname(__file__)

class LoginView:
    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Kirjaudu sisään")
        self.font_main = pygame.font.SysFont('Arial', 30)

        self.position = None
        self.number = None
        self.grid = None

        self.image = pygame.image.load(os.path.join(dirname, "../", "assets", "button.png"))

        self.create_user()

    def create_user(self):
        from ui.ui import Ui

        username_box = TextBox(250,200,200,40)
        password_box = TextBox(250,250,200,40)


        while True:
            self.screen.fill((250, 250, 250))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if create_user_button.is_pressed(
                        pygame.mouse.get_pos()):
                        Ui.menu(self)
                for textbox in [username_box,password_box]:
                    textbox.handle_event(event)
                
            for textbox in [username_box,password_box]:
                textbox.update()

            for textbox in [username_box,password_box]:
                textbox.draw(self.screen)

            register_view_text = self.font_main.render(
                "Kirjaudu sisään", True, (0, 0, 0))
            register_view_text_rect = register_view_text.get_rect(
                center=(275, 150))
            self.screen.blit(register_view_text,
                             register_view_text_rect)
            
            username_text = self.font_main.render(
                "Käyttäjätunnus:", True, (0, 0, 0))
            username_text_rect = username_text.get_rect(
                center=(120, 220))
            self.screen.blit(username_text,
                             username_text_rect)

            password_text = self.font_main.render(
                "Salasana:", True, (0, 0, 0))
            password_text_rect = username_text.get_rect(
                center=(120, 270))
            self.screen.blit(password_text,
                             password_text_rect)

            button_image = pygame.image.load("/home/olkkonso/ot-harjoitustyo/src/button.png")
            button_image = pygame.transform.scale(button_image, (200, 80))
            create_user_button = Button(button_image, 275, 360, "Kirjaudu")
            create_user_button.change_color(pygame.mouse.get_pos())
            create_user_button.update()


            pygame.display.update()
