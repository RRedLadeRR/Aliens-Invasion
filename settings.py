class Settings:
    """Клас для зберігання всіх налаштуваннь гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (128, 0, 0)

        # Параметри корабля
        self.ship_speed = 0.5

        # Параметри снаряду
        self.bullet_speed = 0.25
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_alowed = 30