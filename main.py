import pygame
import sys
import time
import maze

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Scene is to know what scene to show
scene = 0

# Define some fonts
font = pygame.font.SysFont(None, 48)

# Define some text
text = font.render("Main menu", True, BLACK)

# Define some buttons
button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)

# Define some button text
button1_text = font.render("game", True, WHITE)
button2_text = font.render("Maze", True, WHITE)

# Set up the game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if scene == 0: # menu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a button was clicked
                    if button1.collidepoint(event.pos):
                        scene = 0
                    elif button2.collidepoint(event.pos):
                        scene = 3
        elif scene == 1: # sudoku (?)
            '''
            sudoku (?) scene logic
            '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif scene == 2: # meditation (?)
            '''
            meditation (?) scene logic
            '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif scene == 3: # maze
            scene = maze.logic(event)

    # Draw the menu
    if scene == 0: # menu
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, button1)
        pygame.draw.rect(screen, BLACK, button2)
        screen.blit(text, (200, 200))
        screen.blit(button1_text, (215, 260))
        screen.blit(button2_text, (470, 260))
    elif scene == 1: # sudoku (?)
        '''
        sudoku (?) scene graphics
        '''
    elif scene == 2: # meditation (?)
        '''
        meditation (?) scene graphics
        '''
    elif scene == 3: # maze
        '''
        maze scene graphics
        '''
        maze.graphics(screen, font)

    # Update the display
    pygame.display.flip()
