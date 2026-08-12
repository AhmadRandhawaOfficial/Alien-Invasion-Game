import pygame.font
from pygame.sprite import Group
from life_ship import LifeShip


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        self.text_color = 250, 50, 50
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    # Turn the score into a rendered image and initializing its display position.
    def prep_score(self):
        score = int(self.stats.score)
        # rounded_score = int(round(self.stats.score, -1))  # -1 round nears to 10. similarly -3 round nears to 1000.
        score_str = "{:,}".format(score)  # at last we converts it into string.

        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # Initital position.
        self.score_rect.top = 15

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.screen.blit(self.level_img, self.level_rect)

        # Draw ships.
        self.ships.draw(self.screen)

    def prep_high_score(self):
        highscore = int(self.stats.high_score)
        highscore_str = "{:,}".format(highscore)

        self.highscore_img = self.font.render(highscore_str, True, self.text_color, self.ai_settings.bg_color)
        self.highscore_rect = self.highscore_img.get_rect()

        self.highscore_rect.midtop = self.screen_rect.midtop
        self.highscore_rect.top = 15

    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 15
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = LifeShip()
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            self.ships.add(ship)

