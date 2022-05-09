"""
This files contains the class to control what is displayed on screen
"""
import pygame
import constants
pygame.init()


class GraphicsView:
    """
    Display home/start screen, background of game, win/death screen, scores.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """
        Creates a pygame screen
        """
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def _fill_background(self, color):
        """
        Fills the pygame screen with a given color

        Args:
            color: 3 integers rrepresenting the color to fill in the screen
        """
        #Blue = (135, 206, 236)
        self.screen.fill(color)

    def _draw_background(self, img, dims):
        """
        Fills the background of the screen with an image

        Args:
            img: a string representiing the file path to the image
            dims: 2 integers representing the dimensions of the image
        """
        image = pygame.image.load(img)
        rect = image.get_rect()
        image = pygame.transform.scale(image, dims)
        self.screen.blit(image, rect)

    def _draw_group(self, group):
        """
        Draws all the sprites of one group on the pygame screen

        Args:
            group: a pygame group to draw
        """
        group.draw(self.screen)

    def draw_groups(self, groups):
        """
        Draws all sprites from all given groups on screen

        Args:
            groups: a list of groups to draw
        """
        for group in groups:
            self._draw_group(group)

    # pylint: disable=too-many-arguments
    def _display_text(self, text, size, x_pos, y_pos, color=(255, 255, 255)):
        """
        Displays given text on the pygame screen

        Args:
            text: a string containing the text to display
            size: an integer representing font size
            x_pos: an integer representing the x coordinate
            y_pos: an integer representing y coordinate
            color: 3 integers representing the color of the text, defaults
                to white
        """
        font_name = pygame.font.match_font('sarai')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self.screen.blit(text_surface, text_rect)

    def game_display(self, lives, score, groups):
        """
        Displays everything necessary on the main game screen

        Args:
            lives: an integer representing the users lives
            score: an integer reprsenting the users score
            groups: a list of all groups to draw on screen
        """
        self._fill_background((135, 206, 236))
        self._display_text(f"Lives: {lives}", 50,
                           constants.SCREEN_WIDTH - 100, 25, (0, 0, 0))
        self._display_text(f"Score: {score}", 50,
                           constants.SCREEN_WIDTH - 100, 75, (0, 0, 0))
        self.draw_groups(groups)

    def welcome_display(self):
        """
        Displays everything necessary on the welcome screen
        """
        self._fill_background((135, 206, 236))
        self._draw_background('images/Start_screen.png',
                              (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self._display_text("Welcome to Kiki's Delivery Game", 35,
                           constants.SCREEN_WIDTH - 225,
                           constants.SCREEN_HEIGHT-175)
        self._display_text("Press SPACE To Start", 35,
                           constants.SCREEN_WIDTH - 225,
                           constants.SCREEN_HEIGHT-125)

    def end_display(self, score, high_score):
        """
        Displays everything necessary on the end screen

        Args:
            score: an integer reprsenting the users score
        """
        self._fill_background((135, 206, 236))
        self._draw_background('images/End_screen.png',
                              (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self._display_text(f"Your Score: {score}", 50, constants.SCREEN_WIDTH/2,
                           constants.SCREEN_HEIGHT-200)
        self._display_text(f"High Score: {high_score}", 50,
                           constants.SCREEN_WIDTH/2,
                           constants.SCREEN_HEIGHT-150)
        self._display_text("Press SPACE To Play Again", 50,
                           constants.SCREEN_WIDTH/2,
                           constants.SCREEN_HEIGHT-100)
