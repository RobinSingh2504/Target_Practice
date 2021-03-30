import sys

import pygame

from time import sleep

from settings import Settings

from Ship import Ship

from button import rectangle

from rocket import Rocket

from play_button import p_button

from game_stats import Stats


class TargetPractice:

    """The class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game and create the resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Target Practice")

        self.stats = Stats(self)

        self.ship =Ship(self)
        self.rockets = pygame.sprite.Group()
        self.play_button = rectangle(self)
        self.play_but = p_button(self, "Click to Play")

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def _check_rect_edges(self):
        if self.play_button._check_edges():
            self._change_rect_direction()

    def fire_rocket(self):
        if len(self.rockets) <= self.settings.rockets_allowed:
            new_rocket = Rocket(self)
            self.rockets.add(new_rocket)

    def check_play_button(self, mouse_pos):
        #Start a new game when the player clicks Play.
        button_clicked = self.play_but.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game settings
            self.stats.reset_stats()
            self.stats.game_active = True

            self.rockets.empty()

            self.ship.center_ship

            pygame.mouse.set_visible(False)

    def update_rockets(self):
        self.rockets.update()
        for rocket in self.rockets.copy():
            if rocket.rect.right >= self.screen_rect.right:
                self.rockets.remove(rocket)

            self._check_rocket_rect_collisions()

    def target_hit(self):
        self.settings.enhanced_settings()
        self.rockets.empty()
        self.ship.center_ship()
        sleep(0.5)



    def _check_rocket_rect_collisions(self):
        if pygame.sprite.spritecollideany(self.play_button, self.rockets):
            self.target_hit()

    def _change_rect_direction(self):
        self.settings.rect_direction *= -1

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_top = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_rocket()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _run_game(self):
        """Start the main loop of the game. """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_rockets()
                self.update_rect()
            self._update_screen()

    def update_rect(self):
        self._check_rect_edges()
        self.play_button.update()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for rocket in self.rockets.sprites():
            rocket.draw_rocket()
        self.play_button.draw_button()

        if not self.stats.game_active:
            self.play_but.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    tp = TargetPractice()
    tp._run_game()
