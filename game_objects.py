"""

"""
import pygame

class GhibliGameObject(pygame.sprite.Sprite):
    def create_object(self, img, x, y, scale, xflip, yflip):
        """
        Initialize image path, position, hitbox.
        """
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (int(self.img.get_width() * scale), int(self.img.get_height() * scale)))
        self.img = pygame.transform.flip(self.img, xflip, yflip)
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)

class GhibliGameSprite(GhibliGameObject):
    def __init__(self):
        self.create_object('images/kiki.png',100,100,0.5,True,False)

class GhibliGamePackage(GhibliGameObject):
    def __init__(self, y, scale):
        self.create_object('images/kiki.png',700,y,scale,False,False)

class GhibliGameObstacle(GhibliGameObject):
    def __init__(self):
        pass
