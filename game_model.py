import pygame
from game_objects import Geese, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants

pygame.init()

screen = GraphicsView(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
controller = KeyController()
player = Player()

player_group = pygame.sprite.Group()
player_group.add(player)
packages_group = pygame.sprite.Group()
geese_group = pygame.sprite.Group()

fps_clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
package_time = pygame.time.get_ticks()
goose_time = pygame.time.get_ticks()

lives = 3
score = 0

run = True
welcome_screen = True
game_screen = False
end_screen = False

while run:

    while welcome_screen:
        screen.welcome_display()
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            welcome_screen = False
            game_screen = True
            break
        controller.check_exit()

    while game_screen:
        fps_clock.tick(constants.FPS)

        controller.check_exit()

        if pygame.time.get_ticks() - package_time >= 1000:
            package = Packages()
            packages_group.add(package)
            package_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - goose_time >= 1100:
            goose = Geese()
            geese_group.add(goose)
            goose_time = pygame.time.get_ticks()

        pressed_keys = controller.get_move()
        player.move(pressed_keys)

        if player.collide(player_group, packages_group):
            score += 1
        if player.collide(player_group, geese_group):
            lives -= 1

        screen.game_display(
            lives, score, [packages_group, geese_group, player_group])

        if lives == 0:
            game_screen = False
            end_screen = True

        geese_group.update()
        packages_group.update()

        pygame.display.update()

    while end_screen:
        screen.end_display(score)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            lives = 3
            game_screen = True
            end_screen = False
            break
        pygame.display.flip()
        controller.check_exit()

pygame.quit()
