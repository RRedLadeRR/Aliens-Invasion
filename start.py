import sys

import pygame as pg


from alien import Alien

from bullet import Bullet

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
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

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
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагує на натиснення клавіш"""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False         
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _create_alien(self, alien_number, row_number):
        """Створює прибульця і роміщує його в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Створює флот прибульців"""
        # Створення прибульця і визначення кількості прибульців в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        aviable_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = aviable_space_x // (2 * alien_width)

        # Визначення кількості рядів
        ship_height = self.ship.rect.height
        aviable_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = aviable_space_y // (2 * alien_height)
        
        # Створення флоту прибульців
        for row_number in range(number_rows):
            # Створення ряду прибульців
            for alien_number in range (number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _fire_bullet(self):
        """Створює новий снаряд та додає його до групи bulets"""
        if len(self.bullets) < self.settings.bullets_alowed:
            new_bullets = Bullet(self)
            self.bullets.add(new_bullets)

    def _update_bullets(self):
        """Оновлює позиції снарядів"""
        self.bullets.update()
            # Видалення снарядів за краєм екрану
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
            # За кожної ітерації циклу оновлюється екран та Відображення останнього відрендереного екрану
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)

            # Відображення останнього прорисованого екрану
            pg.display.flip()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            self._check_events()
            # Оновлення позиції корабля
            self.ship.update()
            # Оновлення снарядів
            self._update_bullets()
            # За кожної ітерації циклу оновлюється екран та Відображення останнього відрендереного екрану
            self._update_screen()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
