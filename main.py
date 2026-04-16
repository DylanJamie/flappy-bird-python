# main.py
# main application to develop our PI game 

# Import lib
import pygame
import sys
import random

# Set up Constants for the game
pygame.init()
SCREEN        = pygame.display.set_mode((400, 700))
CLOCK         = pygame.time.Clock()
GRAVITY       = 0.25
BIRD_MOVEMENT = 0

# Asset Loading where we can load in the assets from the assets folder
# bird_surface = pygame.image.load('assets/bird.png').convert()
# bg_surface   = pygame.image.load('assets/bg.png').convert()

# Game Function
def draw_pipes(pipes):
    for pipe in pipes: # might switch to while
        # Draw pipes
        pass

# Check if the bird has collided with the pipe
def check_collision(pipes):
    return True

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BIRD_MOVEMENT  = 0
                BIRD_MOVEMENT -= 8

    # Game Logic
    BIRD_MOVEMENT += GRAVITY
    # Update

    # Rendering
    pygame.display.update()
    CLOCK.tick(120)
