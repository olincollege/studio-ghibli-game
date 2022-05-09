"""
Thsi file contains the classes to create sprites used in the game.
"""
import pygame
import random
import constants
pygame.init()


class Objects(pygame.sprite.Sprite):
    """
    This class contains creates and stores information about all the sprites
    used in the game. It has subclasses for players, geese, and packages.
    """

    def create_object(self, img, x, y, scale, xflip, yflip, speed):
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
        self.speed = speed
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (int(
            self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.image = pygame.transform.flip(self.image, xflip, yflip)
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect.center = (x, y)

    def update(self):
        """
        Updates the position of the sprite based on the speed of the sprite
        """
        dx = -self.speed
        self.rect.x += dx
        if self.rect.x < 0 - self.width:
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
        self.y = constants.SCREEN_HEIGHT/2
        self.x = 100
        self.create_object('images/kiki.png', self.x,
                           self.y, 0.5, True, False, 5)

    def move(self, pressed_keys):
        """
        Moves the coordinates of the player sprite based on input from the user

        Args:
            pressed keys: a list of the state of all keys
        """
        dy = 0
        if pressed_keys[pygame.K_UP]:
            dy = -self.speed
        elif pressed_keys[pygame.K_DOWN]:
            dy = self.speed
        self.rect.y += dy

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 800*.8 - self.height:
            self.rect.y = 800*.8 - self.height

    def collide(self, group1, group2):
        """
        Checks if the player sprite has collided with any other sprites

        Args:
            group1: the group containing the player
            group2: the group of objects to check a collision against
        """
        return pygame.sprite.groupcollide(group1, group2, False, True)


class Packages(Objects):
    """
    This class creates an instance of a package and inherits from the objects
        class
    """

    def __init__(self):
        """
        Randomly generates a y coordinate and creates a package sprite
        """
        self.y = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self.create_object('images/Package.png', constants.SCREEN_WIDTH, self.y,
                           0.25, False, False, 2)


class Geese(Objects):
    """
    This class creates an instance of a goose and inherits from the objects
        class
    """

    def __init__(self):
        """
        Randomly generates a y coordinate and creates a goose sprite
        """
        self.y = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self.create_object('images/Goose.png', constants.SCREEN_WIDTH, self.y,
                           0.25, False, False, 3)
