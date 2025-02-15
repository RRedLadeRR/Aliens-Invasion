import pygame as pg


class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує корабель та встановлює цого початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження корабля і отримання поверхні
        self.image = pg.image.load("images/x-wing.png")
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являеться у нижній частині екрану
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Малює корабель в поточній позиції"""
        self.screen.blit(self.image, self.rect)
        