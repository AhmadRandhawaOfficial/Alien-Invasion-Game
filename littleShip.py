import pygame
from pygame.sprite import Sprite
from paths import IMAGE_DIR


class Ship(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_DIR / 'littleShip.png')
        self.rect = self.image.get_rect()
