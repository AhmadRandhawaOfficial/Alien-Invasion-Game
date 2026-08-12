import pygame
from paths import IMAGE_DIR

class Ship():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load(IMAGE_DIR / 'ship.png')
        self.rect = self.image.get_rect()

        # Initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 50

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):  # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Movements with boundary checks
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed

        # Update rect object from self.centerx and self.centery
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 50

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

