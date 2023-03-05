import pygame
import sys
import time
import maze
import sudokuDriver as sd
import sudokuTable as st

# Initialize Pygame
pygame.init()

#name of the app
pygame.display.set_caption("Mental Health games")

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set the fps
FPS = 20
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Scene is to know what scene to show
scene = 0

# Define some fonts
font = pygame.font.SysFont(None, 48)

# Define some text
text = font.render("APPNAME", True, BLACK)

# Define some buttons
button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)
button3 = pygame.Rect(325, 325, 150, 50)

# Define some button text
button1_text = font.render("Sudoku", True, WHITE)
button2_text = font.render("Maze", True, WHITE)
button3_text = font.render("Meditate", True, WHITE)

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
        elif scene == 2: # meditation (?)
            '''
            meditation (?) scene logic
            '''
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif scene == 3: # maze
            maze.logic(event)
            scene = maze.logic(event)
        elif scene == 4: # maze finish screen
            scene = maze.doneLogic(event)

    # Draw the menu
    if scene == 0: # menu
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, button1)
        pygame.draw.rect(screen, BLACK, button2)
        pygame.draw.rect(screen, BLACK, button3)
        screen.blit(text, (200, 200))
        screen.blit(button1_text, (215, 260))
        screen.blit(button2_text, (470, 260))
        screen.blit(button3_text, (330, 335))
    elif scene == 1: # sudoku (?)
        
        sd.printSudoku(screen, sampleSudoku)

        '''
        sudoku (?) scene graphics
        '''
    elif scene == 2: # meditation (?)
        '''
        meditation (?) scene graphics
        '''
    elif scene == 3: # maze
        scene = maze.graphics(event, screen, font)
    elif scene == 4: # maze finish screen
        maze.done(screen, font)

    # Update the display
    pygame.display.flip()
