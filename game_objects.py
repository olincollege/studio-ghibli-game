"""
Thsi file contains the classes to create sprites used in the game.
"""
import random
import pygame
import constants
pygame.init()


def collide(group1, group2):
    """
    Checks if the player sprite has collided with any other sprites

    Args:
        group1: the group containing the player
        group2: the group of objects to check a collision against
    """
    return pygame.sprite.groupcollide(group1, group2, False, True)


class Objects(pygame.sprite.Sprite):  # pylint: disable=too-few-public-methods
    """
    This class contains creates and stores information about all the sprites
    used in the game. It has subclasses for players, geese, and packages.
    """

    def __init__(self):
        """
        Set up the variables for the sprites to be defined in create objects
        """
        self.image = None
        self.rect = None
        self._speed = None
        self._height = None
        self._width = None

    # pylint: disable=too-many-arguments
    def _create_object(self, img, x_pos, y_pos, scale, xflip, yflip, speed):
        """
        create a sprite with given properties

        Args:
            img: a string containing the file path of the iamge
            x: an integer with teh x coordiante of the sprite
            y: an intaeger with the y coordiante of the sprite
            scale: a float representing the desirec scale for the image
            xflip: a bool representing if the image should be flipped over
                the x axis
            yflip: a bool representing if the image should be flipped over
                the y axis
            speed: a integer representing the spped the sprite moves
        """
        pygame.sprite.Sprite.__init__(self)
        self._speed = speed
        image = pygame.image.load(img)
        image = pygame.transform.scale(image,
                                       (int(image.get_width() * scale),
                                        int(image.get_height() * scale)))
        self.image = pygame.transform.flip(image, xflip, yflip)
        self.rect = self.image.get_rect()
        self._height = self.image.get_height()
        self._width = self.image.get_width()
        self.rect.center = (x_pos, y_pos)

    def update(self):
        """
        Updates the position of the sprite based on the speed of the sprite
        """
        # pylint: disable=invalid-name
        dx = -1*self._speed
        self.rect.x += dx
        if self.rect.x < 0 - self._width:
            self.kill()


class Player(Objects):
    """
    This class creates a player and inherits from the objects class
    """

    def __init__(self):
        """
        Sets the x and y coordiantes to be the middle left of the screen and
        creates the player sprite
        """
        super().__init__()
        _y_pos = constants.SCREEN_HEIGHT/2
        _x_pos = 100
        self._create_object('images/kiki.png', _x_pos,
                            _y_pos, 0.5, True, False, 5)

    def move(self, pressed_keys):
        """
        Moves the coordinates of the player sprite based on input from the user

        Args:
            pressed keys: a list of the state of all keys
        """
        dy = 0  # pylint: disable=invalid-name
        if pressed_keys[pygame.K_UP]:
            dy = -1*self._speed    # pylint: disable=invalid-name
        elif pressed_keys[pygame.K_DOWN]:
            dy = self._speed     # pylint: disable=invalid-name
        self.rect.y += dy

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 800*.8 - self._height:
            self.rect.y = 800*.8 - self._height


class Packages(Objects):  # pylint: disable=too-few-public-methods
    """
    This class creates an instance of a package and inherits from the objects
        class
    """

    def __init__(self):
        """
        Randomly generates a y coordinate and creates a package sprite
        """
        super().__init__()
        _y_pos = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self._create_object('images/Package.png', constants.SCREEN_WIDTH,
                            _y_pos, 0.25, False, False, 2)


class Geese(Objects):  # pylint: disable=too-few-public-methods
    """
    This class creates an instance of a goose and inherits from the objects
        class
    """

    def __init__(self):
        """
        Randomly generates a y coordinate and creates a goose sprite
        """
        super().__init__()
        _y_pos = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self._create_object('images/Goose.png', constants.SCREEN_WIDTH, _y_pos,
                            0.25, False, False, 3)
