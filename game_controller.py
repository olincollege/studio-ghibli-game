"""
This files has a controller for the game.
"""
import pygame
pygame.init()


class KeyController():
    """
    This class contains fucntions controlling how the user interacts with
    the game.
    """

    # pylint: disable=no-self-use
    def get_move(self):
        """
        Return a list of all of the pressed keys

        Args:
            none
        Returns:
            a list of the current state of all keys on the keyboard
        """
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    # pylint: disable=no-self-use
    def check_exit(self):
        """
        Checks if the player has clicked the X and exits pygame if they have.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
