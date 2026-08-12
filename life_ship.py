import pygame
from pygame.sprite import Sprite
from paths import IMAGE_DIR


class LifeShip(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_DIR / 'life_ship.png')
        self.rect = self.image.get_rect()
