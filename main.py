# import dependencies
import sys
import pygame

# import game parts
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overal class to manage game assests and behaviro"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # set ship
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # redraw the screen during each pass through the loop 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # make most recently drawn screen visable
        pygame.display.flip()
    
if __name__ == '__main__':
    # mak a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
