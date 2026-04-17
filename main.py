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
            if event.key == pygame.K_SPACE:
                if game_active:
                    bird_movement  = 0
                    bird_movement -= 8
                else:
                    game_active = True
                    bird_rect.center = (100, 350)
                    bird_movement  = 0

    if game_active:
        # Game Logic
        bird_movement += gravity
        bird_rect.centery += bird_movement
        # Update
        # Rendering
        screen.fill(sky_blue)
        # Draw the bird
        pygame.draw.rect(screen, yellow, bird_rect)

        # Check if the bird hit the top or bottom of the screen
        if bird_rect.top <= 0 or bird_rect.bottom >= 700:
            game_active = False
    else:
        # this is an RGB Color | RED
        screen.fill((200, 0, 0))
    
    pygame.display.update()
    clock.tick(120)
