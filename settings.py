class Settings:
    """Клас для зберігання всіх налаштуваннь гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (128, 0, 0)

        # Параметри корабля
        self.ship_speed = 2.5 # 0.5
        self.ship_limit = 3

        # Параметри снаряду
        self.bullet_speed = 2 # 0.25
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_alowed = 128

        # Параметри прибульців
        self.alien_speed = 1 # 0.1
        self.fleet_drop_speed = 10 # 1
        # fleet_direction = 1 якщо флот рухаеться праворуч, -1 якщо ліворуч
        self.fleet_direction = 1