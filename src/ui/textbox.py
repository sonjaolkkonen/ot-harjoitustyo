import pygame


class TextBox:
    """Luokka, joka luo rekistetöitymis- ja kirjautumis-näkymissä käytetyn tekstikentän. 
    """

    def __init__(self, x, y, w, h, text=''):
        """Luokan konstruktori, joka luo tekstikentän.

        Args:
            x: Tekstikentän x-akselin sijainti. 
            y: Tekstikentän y-akselin sijainti.
            w: Tekstikentän leveys.
            h: Tekstikentän korkeus.
            text: Tekstikentän teksti, joka on oletusarvoltaan tyhjä. 
        """

        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.textbox_font = pygame.font.SysFont('Arial', 20)

        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.text_surface = self.textbox_font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """Käsittelee luokan tapahtumat. Mikäli tekstikenttää klikataan, vaihtuu sen väri ja pelaaja pystyy kirjoittamaan kenttään. Päivittää tekstikenttään kirjoitetun tekstin.

        Args:
            event: Tapahtuma, joka tapahtuu.  
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = self.textbox_font.render(self.text, True,(0,0,0))

    def update(self):
        """Päivittää tekstikentän leveyden, mikäli teksti menee tekstikentän yli. 
        """
        width = max(200, self.text_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        """Piirtää tekstikentän sekä tekstin näytölle. 

        Args:
            screen: Näyttö. 
        """
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)




