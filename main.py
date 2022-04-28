import pygame
from game_objects import GhibliGameObject, GhibliGamePackage, GhibliGameSprite

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = GhibliGameSprite()
package = GhibliGamePackage(500,0.25)

run = True

while run:

    screen.blit(player.img, player.rect)
    screen.blit(package.img,package.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()