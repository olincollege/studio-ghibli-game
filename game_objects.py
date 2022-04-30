"""

"""
import pygame

pygame.init()


class GhibliGameObject(pygame.sprite.Sprite):
    def create_object(self, img, x, y, scale, xflip, yflip, speed):
        """
        Initialize image path, position, hitbox.
        """
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (int(
            self.img.get_width() * scale), int(self.img.get_height() * scale)))
        self.img = pygame.transform.flip(self.img, xflip, yflip)
        self.rect = self.img.get_rect()
        self.height = self.img.get_height()
        self.rect.center = (x, y)

    def move(self):
        dx = -self.speed
        self.rect.x += dx


class GhibliGameSprite(GhibliGameObject):
    def __init__(self):
        self.create_object('images/kiki.png', 100, 100, 0.5, True, False, 5)

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


class GhibliGamePackage(GhibliGameObject):
    def __init__(self, y, scale, speed):
        self.create_object('images/Package.png', 700, y,
                           scale, False, False, speed)


class GhibliGameObstacle(GhibliGameObject):
    def __init__(self, y, scale, speed):
        self.create_object('images/Goose.png', 700, y,
                           scale, False, False, speed)
