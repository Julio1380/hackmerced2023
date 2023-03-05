import pygame
import sys
import time
import maze
import sudokuDriver as sd
import sudokuTable as st
import Meditation

# Initialize Pygame
pygame.init()

#name of the app
pygame.display.set_caption("Mindset")

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set the fps
FPS = 20
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PASTEL = (255, 202, 175)
PURUPLE = (224, 187, 228)
BG = (240, 220, 240)

# Scene is to know what scene to show
scene = 0

# Define some fonts
font = pygame.font.SysFont('lucida calligraphy', 25)
title = pygame.font.SysFont('lucida calligraphy', 50)

# Define some text
text = title.render("Mindset", True, BLACK)

# Define some buttons
button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)
button3 = pygame.Rect(325, 325, 150, 50)

# Define some button text
button1_text = font.render("Sudoku", True, BLACK)
button2_text = font.render("Maze", True, BLACK)
button3_text = font.render("Meditate", True, BLACK)

#meditation object, initalized in event handle
meditation = None

# Sudoku Table
sampleSudoku = st.sudoku()

# Set up the game loop
while True:
    
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if scene == 0: # menu
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a button was clicked
                    if button1.collidepoint(event.pos):
                        scene = 1
                    elif button2.collidepoint(event.pos):
                        scene = 3
                        maze.block.x = 0
                        maze.block.y = 260
                    elif button3.collidepoint(event.pos):
                        scene = 2
                        meditation = Meditation.Meditation(screen, font)
                    
        elif scene == 1: # sudoku (?)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                scene = sd.runSudoku(event, sampleSudoku)
            '''
            sudoku (?) scene logic
            '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif scene == 2: # meditation
            scene = meditation.handleEvent(event)
        elif scene == 3: # maze
            maze.logic(event)
            scene = maze.logic(event)
        elif scene == 4: # maze finish screen
            scene = maze.doneLogic(event)

    # Draw the menu
    if scene == 0: # menu
        screen.fill(PASTEL)
        pygame.draw.rect(screen, PURUPLE, button1)
        pygame.draw.rect(screen, PURUPLE, button2)
        pygame.draw.rect(screen, PURUPLE, button3)
        screen.blit(text, (300, 150))
        screen.blit(button1_text, (215, 260))
        screen.blit(button2_text, (470, 260))
        screen.blit(button3_text, (330, 335))
    elif scene == 1: # sudoku (?)
        
        sd.printSudoku(screen, sampleSudoku)

        '''
        sudoku (?) scene graphics
        '''
    elif scene == 2: # meditation (?)
        meditation.draw()
    elif scene == 3: # maze
        scene = maze.graphics(event, screen, font)
    elif scene == 4: # maze finish screen
        maze.done(screen, font)

    # Update the display
    pygame.display.flip()
