import pygame
from pygame.sprite import Sprite
from paths import IMAGE_DIR


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(IMAGE_DIR / "alien.png")
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.ai_settings.fleet_speed * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True

        elif self.rect.left <= self.screen_rect.left:
            return True
