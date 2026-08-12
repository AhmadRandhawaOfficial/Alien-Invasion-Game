import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb):
    # KEYDOWN and KEYUP used together for continues motion.
    for event in pygame.event.get():  # Watch for keyboard and mouse events.
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, bullets, aliens, stats, play_button, mousex, mousey, sb)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_SPACE:  # Whenever, we pressed space, 1 bullet will be stored in bullets().
        if len(bullets) < ai_settings.bullets_allowed:  # Initially, bullets is empty, so len(bullets) is 0.
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)  # if you used rect there like in button, then only specific area will be covered.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()  # Make the most recently drawn screen visible.


def update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb):
    bullets.update()  # it is actually equals to    [for bullet in bullets.sprites(): bullet.update()]

    # Get rid of bullets that have disappeared.
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, stats, sb)


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    aliens_per_row = get_aliens_per_row(ai_settings, alien_width)
    aliens_row = get_alien_row(ai_settings, alien.rect.height, ship.rect.height)

    for alien_row in range(aliens_row):
        for alien_per_row in range(aliens_per_row):
            create_alien(ai_settings, screen, alien_width, alien_per_row, aliens, alien_row)


def get_aliens_per_row(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    aliens_per_row = int(available_space_x / (2 * alien_width))
    return aliens_per_row


def create_alien(ai_settings, screen, alien_width, alien_per_row, aliens, alien_row):
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_per_row
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_row
    aliens.add(alien)


def get_alien_row(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - 3 * alien_height) - ship_height
    aliens_row = int(available_space_y / (2 * alien_height))
    return aliens_row


def update_aliens(ai_settings, screen, ship, bullets, aliens, stats, sb):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    check_alien_ship_hit(ai_settings, screen, ship, bullets, aliens, stats, sb)
    check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, stats, sb)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():  # Check to see if at least 1 alien is collided with edge of the screen.
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, stats, sb):
    # group collide returns a dictionary. where bullets are keys and aliens are values.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def ship_hit(ai_settings, screen, ship, bullets, aliens, stats, sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1  # Decrement 1 ship after every hit.
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)  # A new fleet of aliens
        ship.center_ship()
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_alien_ship_hit(ai_settings, screen, ship, bullets, aliens, stats, sb):
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, ship, bullets, aliens, stats, sb)


def check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, stats, sb):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, ship, bullets, aliens, stats, sb)  # Treat this as same as if the ship got hit
            return

def check_play_button(ai_settings, screen, ship, bullets, aliens, stats, play_button, mousex, mousey, sb):
    button_clicked = play_button.rect.collidepoint(mousex, mousey)  # Return True if any point collides with button rect

    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()  # Reset the game settings.
        pygame.mouse.set_visible(False)  # Hiding the mouse cursor.

        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
