"""

"""
import pygame
import random
import constants

pygame.init()


class Objects(pygame.sprite.Sprite):
    def create_object(self, img, x, y, scale, xflip, yflip, speed):
        """
        Initialize image path, position, hitbox.
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
        dx = -self.speed
        self.rect.x += dx
        if self.rect.x < 0 - self.width:
            self.kill()


class Player(Objects):
    def __init__(self):
        self.y = constants.SCREEN_HEIGHT/2
        self.x = 100
        self.create_object('images/kiki.png', self.x,
                           self.y, 0.5, True, False, 5)

    def move(self, pressed_keys):
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


class Packages(Objects):
    def __init__(self, speed):
        self.y = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self.create_object('images/Package.png', constants.SCREEN_WIDTH, self.y,
                           0.25, False, False, speed)


class Geese(Objects):
    def __init__(self, speed):
        self.y = (random.randint((0 + constants.PACKAGE_HEIGHT)/10,
                  (constants.SCREEN_HEIGHT-constants.PACKAGE_HEIGHT)/10))*10
        self.create_object('images/Goose.png', constants.SCREEN_WIDTH, self.y,
                           0.25, False, False, speed)
