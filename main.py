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
# keep track of which pipes have counted as a score
scored_pipes = []


# Colors
sky_blue = (135, 206, 235)
yellow   = (255, 255,   0)
black    = (0,     0,   0)
white    = (255, 255, 255)
green    = (80,  200, 120)

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('./assets/ARCADECLASSIC.TTF', 32)

# Draw the pipes
# make a list for the pipes and have a new pipe spawn in every 1.2 sec
# Make the pipe height random between any of the listed heights
pipe_list = []
pipe_time = 1200
spawn_pipe = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe, pipe_time)
pipe_height = [300, 400, 500]

# Updating the collisions function
def check_collisions(pipes):
    for pipe in pipes:
        # If the bird colides with the pipe return false
        if bird_rect.colliderect(pipe):
            return False
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
        if event.type == spawn_pipe:
            random_pipe_position = random.choice(pipe_height)
            # Create a new pipe to try and effect the player
            new_pipe = pygame.Rect(500, random_pipe_position, 50, 500)
            pipe_list.append(new_pipe)

    if game_active:
        # Game Logic
        bird_movement += gravity
        bird_rect.centery += bird_movement
        # Update
        # Rendering
        screen.fill(sky_blue)
        # Draw the bird
        pygame.draw.rect(screen, yellow, bird_rect)
            
        # Render the Init_Score text
        score_text = font.render(f"{init_score}", True, white)
                
        # create a rectangular object for the
        # text surface object
        score_textRect = score_text.get_rect()

        # set the center of the rectangular object.
        score_textRect.center = (X // 2, 50)

        # Draw the Score on the Game
        screen.blit(score_text, score_textRect)
        
        # Pipe Logic
        for pipe in pipe_list:
            # Move the pipe to the left
            pipe.centerx -= 5
            # Draw the pipe
            pygame.draw.rect(screen, green, pipe)
            
            # Update score
            if bird_rect.left >= pipe.right:
                if pipe not in scored_pipes:
                    init_score += 1
                    scored_pipes.append(pipe)

        # Check for collison
        game_active = check_collisions(pipe_list)

        # Check if the bird hit the top or bottom of the screen
        if bird_rect.top <= 0 or bird_rect.bottom >= 700:
            game_active = False
        
        # Remove pipe that goes off the screen to save memory
        # Create a temp list
        remaining_pipes = []

        # loop throught the current pipes
        for pipe in pipe_list:
            # If the Pipe is still on the screen keep it
            if pipe.right > -50:
                remaining_pipes.append(pipe)

        # over write the list with an updated one
        pipe_list = remaining_pipes
        # Conclude memory clean up
        
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

        # clear the pipe list
        pipe_list.clear()
        
        # clear the scored pipe list
        scored_pipes.clear()
        
    pygame.display.update()
    clock.tick(120)
