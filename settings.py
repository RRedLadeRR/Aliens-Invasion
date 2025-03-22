class Settings:
    """Клас для зберігання всіх налаштуваннь гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (128, 0, 0)

        # Параметри корабля
        self.ship_limit = 3

        # Параметри снаряду
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_alowed = 128

        # Параметри прибульців
        self.fleet_drop_speed = 10 # 1

        # Темп пришвидшення гри
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізує налаштування що змінюються під час гри"""
        # Параметри корабля
        self.ship_speed_factor = 2.5 # 0.5

        # Параметри снаряду
        self.bullet_speed_factor = 2 # 0.25

        # Параметри прибульців
        self.alien_speed_factor = 1 # 0.1

        # fleet_direction = 1 якщо флот рухаеться праворуч, -1 якщо ліворуч
        self.fleet_direction = 1

        # Підрахунок очок
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
