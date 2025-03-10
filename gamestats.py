class GameStats:
    """Відслідковування статистики гри"""

    def __init__(self, ai_game):
        """Ініціалізує статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Ініціалізує статистику, що змінюється під час гри"""
        self.ships_left = self.settings.ship_limit
