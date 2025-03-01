import sys

import pygame as pg

from settings import Settings

from ship import Ship


class AlienInvasion:
    """Клас для управління ресурсами та поведікою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()
        self.settings = Settings()

        # self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN) # Fullscreen
        self.settings.screen_width = self.screen.get_rect().width # Fullscreen
        self.settings.screen_height = self.screen.get_rect().height # Fullscreen
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def _check_events(self):
        """Обробляє натиснення клавіш та подій миші"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагує на натиснення клавіш"""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагує на натиснення клавіш"""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False         
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
            # За кожної ітерації циклу оновлюється екран та Відображення останнього відрендереного екрану
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pg.display.flip()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            self._check_events()
            # Оновлення позиції корабля
            self.ship.update()
            # За кожної ітерації циклу оновлюється екран та Відображення останнього відрендереного екрану
            self._update_screen()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
