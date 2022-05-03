import pygame
from game_objects import Geese, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants

pygame.init()

screen = GraphicsView(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
controller = KeyController()
player = Player()
objects_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_group.add(player)
packages_group = pygame.sprite.Group()
geese_group = pygame.sprite.Group()

fps_clock = pygame.time.Clock()
lives = 3
score = 0
start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()

run = True
welcome_screen = True
game_screen = True
end_screen = True

while run:
    while welcome_screen:
        screen.fill_background((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                welcome_screen = False
                print(True)
                break
            if event.type == pygame.QUIT:
                run = False

    while run:
        fps_clock.tick(constants.FPS)
        screen.fill_background((135, 206, 236))
        if pygame.time.get_ticks() - current_time >= 5000:
            package = Packages(2)
            packages_group.add(package)
            goose = Geese(2)
            geese_group.add(goose)
            current_time = pygame.time.get_ticks()

        screen.draw_group(packages_group)
        screen.draw_group(geese_group)
        screen.draw_group(player_group)

        pressed_keys = controller.get_move()
        player.move(pressed_keys)

        if pygame.sprite.groupcollide(player_group, packages_group, False, True):
            score += 1
        if pygame.sprite.groupcollide(player_group, geese_group, False, True):
            lives -= 1

        screen.display_text(f"Lives: {lives}", 50,
                            constants.SCREEN_WIDTH - 100, 25)
        screen.display_text(f"Score: {score}", 50,
                            constants.SCREEN_WIDTH - 100, 75)

        if lives == 0:
            run = False

        geese_group.update()
        packages_group.update()

        pygame.display.update()

        #if pygame.time.get_ticks() >= 5000:
        #    run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

pygame.quit()
