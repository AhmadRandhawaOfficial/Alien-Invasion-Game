import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # It is a surface.
    pygame.display.set_icon(ai_settings.game_icon)
    pygame.display.set_caption(ai_settings.game_name)

    stats = GameStats(ai_settings)
    play_button = Button(screen, "Start")
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)  # Used to stored number of aliens there, in Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)
        if stats.game_active:
            ship.update()  # update, used for movements
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings, screen, ship, bullets, aliens, stats, sb)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)  # Used for drawing.
        clock.tick(60)


run_game()
