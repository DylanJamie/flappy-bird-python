# main.py
# main application to develop our PI game 

# Import lib
import pygame
import sys
import random

# Set up Constants for the game
pygame.init()
X = 400
Y = 700
screen        = pygame.display.set_mode((X, Y))
clock         = pygame.time.Clock()

# Game Variables
gravity       = 0.25
bird_movement = 0
game_active   = True
# Create a Rectangle for the bird (x, y, width, height)
bird_rect = pygame.Rect(100, 350, 30, 30) 
init_score = 0

# Colors
sky_blue = (135, 206, 235)
yellow   = (255, 255,   0)
black    = (0,     0,   0)
white    = (255, 255, 255)

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('./assets/ARCADECLASSIC.TTF', 32)

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

        # Display a score at the top of the game
        if bird_rect.top <= 400:
            init_score += 1
            
        # Render the Init_Score text
        score_text = font.render(f"{init_score}", True, white)
                
        # create a rectangular object for the
        # text surface object
        score_textRect = score_text.get_rect()

        # set the center of the rectangular object.
        score_textRect.center = (X // 2, 50)

        # Draw the Score on the Game
        screen.blit(score_text, score_textRect)
        
        # Check if the bird hit the top or bottom of the screen
        if bird_rect.top <= 0 or bird_rect.bottom >= 700:
            game_active = False
    else:
        # this is an RGB Color | RED
        screen.fill((200, 0, 0))

        # create a text surface object,
        # on which text is drawn on it.
        gameover_text = font.render('Game Over', True, black)

        # create a rectangular object for the
        # text surface object
        gameover_textRect = gameover_text.get_rect()
        
        # set the center of the rectangular object.
        gameover_textRect.center = (X // 2, Y // 2)
        
        # show the game over in the center (Draw on the Text)
        screen.blit(gameover_text, gameover_textRect)

        # Set the score to 0
        init_score = 0
        
    pygame.display.update()
    clock.tick(120)
