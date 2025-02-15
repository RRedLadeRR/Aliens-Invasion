import sys

import pygame


class AlienInvasion:
    """Клас для управління ресурсами та поведікою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Відображення останнього відрендереного екрану
            pygame.display.flip()


if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
