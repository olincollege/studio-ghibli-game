import pytest
import pygame
import operator
from game_objects import Player, Geese, Packages

pygame.init()

test_player = Player()
test_goose = Geese()
test_package = Packages()

player_group = pygame.sprite.Group()
player_group.add(test_player)
packages_group = pygame.sprite.Group()
player_group.add(test_goose)
geese_group = pygame.sprite.Group()
player_group.add(test_package)

update_cases = [
    # test that geese and pacakges move to the left when updated
    test_goose,
    test_package
]

Up_dictionary = {
    pygame.K_UP: True
}
Down_dictionary = {
    pygame.K_DOWN: True,
    pygame.K_UP: False
}
Both_dictionary = {
    pygame.K_UP: True,
    pygame.K_DOWN: True
}
Space_dictionary = {
    pygame.K_SPACE: True,
    pygame.K_UP: False,
    pygame.K_DOWN: False
}
move_cases = [
    # test that the player moves up when up is pressed
    (test_player, Up_dictionary, operator.lt),
    # test that the player moves down when down is pressed
    (test_player, Down_dictionary, operator.gt),
    # test that the player moves up when both pressed
    (test_player, Both_dictionary, operator.lt),
    # test that the player does not move when none are pressed
    (test_player, Space_dictionary, operator.eq)
]

collision_player = Player()
collision_group = pygame.sprite.Group()
collision_group.add(collision_player)
collide_cases = [
    # test that the player collides with a coincident sprite
    (player_group, collision_group, {test_player: [collision_player]}),
    # test that the player does not colide with a non-coincident sprite
    (player_group, geese_group, {}),
]


@pytest.mark.parametrize("sprite", update_cases)
def test_update(sprite):
    current_x = sprite.rect.x
    sprite.update()
    assert current_x > sprite.rect.x


@pytest.mark.parametrize("sprite, dictionary, relate", move_cases)
def test_move(sprite, dictionary, relate):
    current_y = sprite.rect.y
    sprite.move(dictionary)
    assert relate(sprite.rect.y, current_y) == True


@pytest.mark.parametrize("group_1, group_2, dictionary", collide_cases)
def test_collide(group_1, group_2, dictionary):
    assert test_player.collide(group_1, group_2) == dictionary
