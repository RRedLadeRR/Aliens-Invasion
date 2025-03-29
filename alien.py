import pygame as pg
from pygame.sprite import Sprite

W = 64
H = 64

class Alien(Sprite):
    """Клас для прибульця"""

    def __init__(self, ai_game):
        """Ініціалізує прибульця та задає його початкову позіцію"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантаження зображення прибульця та визначення rect
        filename = ("images/" + "tie-fighter.png" if self.settings.dark_mode else "tie-fighter.png")
        self.image = pg.transform.scale(pg.image.load(filename), (W, H))
        self.rect = self.image.get_rect()

        # Кожен новий прибулець з'являеться в лівому верхньому куті екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)

    def check_edges(self):
        """Повертає Trueб якщо прибулець біля краю екрану"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Переміщує прибульця праворуч"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x