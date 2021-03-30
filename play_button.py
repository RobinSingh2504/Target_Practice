import pygame.font  #pygame rendering text on the screen.

class p_button:

    def __init__(self, tp_game, msg):
        """Initialize the button assets."""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()


        #Set the dimensions and properties of the button.

        self.width, self.height =200, 50
        self.button_color = (0,250,0)
        self.text_color = (255,255,255)

        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg) #Pygame works with text by rendering the string you want to display as an image.

    def prep_msg(self, msg):
        """Turn the message into a rendered image and center the text on the screen."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect =self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw a blank button and then draw the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)