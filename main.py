# main.py
# main application to develop our PI game 

# Import lib
import pygame
import sys
import random

# Set up Constants for the game
pygame.init()
screen        = pygame.display.set_mode((400, 700))
clock         = pygame.time.Clock()

# Game Variables
gravity       = 0.25
bird_movement = 0
game_active   = True
# Create a Rectangle for the bird (x, y, width, height)
bird_rect = pygame.Rect(100, 350, 30, 30) 

# Colors
sky_blue = (135, 206, 235)
yellow   = (255, 255,   0)

# Asset Loading where we can load in the assets from the assets folder
# bird_surface = pygame.image.load('assets/bird.png').convert()
# bg_surface   = pygame.image.load('assets/bg.png').convert()

# # Game Function
# def draw_pipes(pipes):
#     for pipe in pipes: # might switch to while
#         # Draw pipes
#         pass

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
            if event.key == pygame.K_SPACE and game_active:
                bird_movement  = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True

    # Update the positions
    # Draw everything
    # check the collisions
    # if game_active:
    #     if check_collision(pipes):
    #         # the loop will continue but the logic will pause
    #         game_active = False
    # else:
    #     # Show the game over or "PRess Space to restart"
    #     pass
            
    # Game Logic
    bird_movement += gravity
    bird_rect.centery += bird_movement
    # Update

    # Rendering
    screen.fill(sky_blue)
    # Draw the bird
    pygame.draw.rect(screen, yellow, bird_rect)
    
    pygame.display.update()
    clock.tick(120)
