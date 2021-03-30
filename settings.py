import  pygame

class Settings:
    """This is a class to store all the game settings for Target Practice. """

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Define ship speed

        self.ship_limit = 2

        #Rectangle speed

        self.rect_direction = 1

        #Rocket settings

        self.rocket_width = 45
        self.rocket_height = 5
        self.rocket_color = (60,60,60)
        self.rockets_allowed = 2

        self.speed_scale = 1.1

        self.rocket_speed = 2
        self.ship_speed = 1
        self.rect_speed = 3


    def enhanced_settings(self):
        self.rocket_speed *= self.speed_scale
        self.ship_speed *= self.speed_scale
        self.rect_speed *= self.speed_scale

