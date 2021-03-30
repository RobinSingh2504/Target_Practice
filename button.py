import pygame.font


class rectangle:

    def __init__(self, tp_game):
        """Initialize the button assets"""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings

        ##Set the dimensions of the rectangle

        self.width, self.height = 100, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        ##Building the button's rect object and then putting it on the edge.
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        self.rect.y = self.rect.height

        #floating position
        self.y=float(self.rect.y)

    def draw_button(self):
        #Draw a blank button
        self.screen.fill(self.button_color, self.rect)

    def _check_edges(self):
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top < 0:
            return True

    def update(self):
        self.y += (self.settings.rect_speed * self.settings.rect_direction)
        self.rect.y = self.y

