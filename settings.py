class Settings:

    def __init__(self):
        # screen settings initialise 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)


        # ship settings 
        # self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings 
        # self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3 

        # Alien Settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        # self.fleet_direction = 1

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # how quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        # initialize setings thay change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction of 1 represents right : -1 represents left
        self.fleet_direction = 1

        # scoring 
        self.alien_points = 50


    def increase_speed(self):
        # increase speed settings and alien point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        





