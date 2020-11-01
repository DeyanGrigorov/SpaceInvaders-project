import random

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Adding Background
background = pygame.image.load('background.jpg')

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Millenium_Falcon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('Player.png')
player_X = 370
player_Y = 480
player_X_change = 0
player_Y_change = 0

# enemy
enemy_img = pygame.image.load('enemy.png')
enemy_X = random.randint(0, 800)
enemy_Y = random.randint(50, 150)
enemy_X_change = 2
enemy_y_change = 40


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


running = True
while running:
    # RGB - RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_change = -5
            if event.key == pygame.K_RIGHT:
                player_X_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_X_change = 0

    # Checking for boundaries
    player_X += player_X_change
    if player_X <= 0:
        player_X = 0
    elif player_X >= 736:
        player_X = 736

    # Enemy movement
    enemy_X += enemy_X_change
    if enemy_X <= 0:
        enemy_X_change = 2
        enemy_Y += enemy_y_change
    elif enemy_X >= 736:
        enemy_X_change = -2
        enemy_Y += enemy_y_change

    player(player_X, player_Y)
    enemy(enemy_X, enemy_Y)

    pygame.display.update()

