class Settings:
    """A class to stroe all settings for game"""

    def __init__(self):
        """Initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

         # setting speed 
        self.ship_speed = 4

        # setting bullet information
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 4


