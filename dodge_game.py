# Name:
# Date:
# Pygame Dodge Game

"""
Student Skeleton: Pygame Dodge Game

Follow the README steps and fill in or customize each TODO section.
"""

import pygame
import random


# Step 3: Initialize Pygame
pygame.init()

WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")

clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 255)
RED = (255, 60, 60)
GREEN = (0, 255, 0)
PURPLE = (157,0,255)
running = True
game_over = False

restart_button_rect = pygame.Rect(350, 250, 100, 50)
player_width = 60
player_height = 60

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 90

player_speed = 7

player_width = 60
player_height = 60

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 90

object_width = 50
object_height = 50

object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height

object_speed = 5

object2_x = random.randint(0, WIDTH - object_width)
object2_y = -200
object2_speed = 6

object3_x = random.randint(0, WIDTH - object_width)
object3_y = -400
object3_speed = 7

object4_x = random.randint(0, WIDTH - object_width)
object4_y = -400
object4_speed = 7
winning_score = 10
score = 0
font = pygame.font.SysFont(None, 36)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))
    pygame.draw.rect(screen, BLACK, (object2_x, object2_y, object_width, object_height))
    pygame.draw.rect(screen, GREEN, (object3_x, object3_y, object_width, object_height))
    pygame.draw.rect(screen, PURPLE, (object4_x, object4_y, object_width, object_height))
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))
    if game_over:
        game_over_text = font.render("GAME OVER DIDDYBLUD", True, BLACK)
        restart_text = font.render("Close the window to quit.", True, BLACK)

        screen.blit(game_over_text, (WIDTH // 2 - 90, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 2 - 140, HEIGHT // 2 + 10))
    if score >= winning_score:
        game_over = True
        victory_text = font.render("CONGRATS YOU WIN", True, BLACK)
    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if player_x < 0:
            player_x = 0

        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width
        object_y += object_speed
        if object_y > HEIGHT:
            object_y = -object_height
            object_x = random.randint(0, WIDTH - object_width)
            score += 1
        if object2_y > HEIGHT:
            object2_y = -object_height
            object2_x = random.randint(0, WIDTH - object_width)
            score += 1
        if object3_y > HEIGHT:
            object3_y = -object_height
            object3_x = random.randint(0, WIDTH - object_width)
            score += 1
        if object4_y > HEIGHT:
            object4_y = -object_height
            object4_x = random.randint(0, WIDTH - object_width)
            score += 1
        object_y += object_speed
        object2_y += object2_speed
        object3_y += object3_speed
        object4_y += object4_speed
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
        object2_rect = pygame.Rect(object2_x, object2_y, object_width, object_height)
        object3_rect = pygame.Rect(object3_x, object3_y, object_width, object_height)
        object4_rect = pygame.Rect(object4_x, object4_y, object_width, object_height)
        if player_rect.colliderect(object_rect) or player_rect.colliderect(object2_rect) or player_rect.colliderect(object3_rect) or player_rect.colliderect(object4_rect):
            game_over = True
    pygame.display.update()

pygame.quit()