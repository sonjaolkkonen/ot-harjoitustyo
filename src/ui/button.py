import pygame

pygame.init()

screen = pygame.display.set_mode((550, 550))
main_font = pygame.font.SysFont('Arial', 30)

class Button:
    """Luokka, joka luo sovelluksen käyttöliittymässä käytettävän painikkeen.
    """
    def __init__(self, image, x_pos, y_pos, content):
        """Luokan konstruktori, joka luo painikkeen.

        Args:
            image: Painikkeen kuva.
            x_pos: Painikkeen x-akselin sijainti.
            y_pos: Painikkeen y-akselin sijainti.
            content: Painikkeessa näkyvä teksti.
        """
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
        """Päivittää painikkeessa näkyvän tekstin sekä itse painikkeen.
        """
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def is_pressed(self, position):
        """Tarkistaa sijainnin avulla onko painiketta painettu.

        Args:
            position: Painikkeen sijainti.

        Returns:
            True, jos painiketta on painettu, muussa tapauksessa False.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        """Vaihtaa painikkeen tekstin väriä mikäli kursori on painikkeen päällä. 

        Args:
            position: Painikkeen sijainti. 
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.content, True, (0,0,0))
        else:
            self.text = main_font.render(self.content, True, (255,255,255))



