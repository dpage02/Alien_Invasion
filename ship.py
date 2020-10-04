import pygame
from PIL import Image

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initiallize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the original image, change to wanted to dimensions and load for pygame 
        self.image = Image.open('images/buzz.png')
        self.new_image = self.image.resize((80,80))
        self.new_image.save('images/img_300.png')
        self.image = pygame.image.load('images/img_300.png')
        self.rect = self.image.get_rect()

        # start each new ship at the nottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value fo ship's horizontal position
        self.x = float(self.rect.x)

        # movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flags"""
        # update ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 

        # update rect oject from the self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)