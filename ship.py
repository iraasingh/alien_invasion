import pygame 
class Ship:
    def __init__(self, ai_game):
        # initialise the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect()
    

        # load the ship image and get its rect.
        #self.image = pygame.image.load('images/ship.bmp')
        original_image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(original_image, (60, 48))  # Width: 60px, Height: 48px

        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship horizontal position.
        self.x = float(self.rect.x)

        # movement flag 
        self.moving_right = False 
        self.moving_left = False 
    
    def update(self):
        # update ship's position based on the movement flag
        # update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # update rect object from sefl.x.
        self.rect.x = self.x


    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

        