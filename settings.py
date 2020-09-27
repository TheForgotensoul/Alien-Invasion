
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullet_allowed = 3
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.intialize_dynamic_settings()

    def intialize_dynamic_settings(self):

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

