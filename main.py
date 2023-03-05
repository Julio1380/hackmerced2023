import pygame
import sys
import time
import maze
import sudokuDriver as sd
import sudokuTable as st
import Meditation as med

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

# buttons used for meditation
meditationButton1 = pygame.Rect(325, 520, 150, 50)

# Define some button text
button1_text = font.render("Sudoku", True, WHITE)
button2_text = font.render("Maze", True, WHITE)
button3_text = font.render("Meditate", True, WHITE)

#define some text used for the meditation scence
meditationWelcome1 = font.render("meditation time", True, BLACK)
meditationWelcome2 = font.render("Deep breathing relaxes the body. Ready to start?", True, BLACK)
meditationStartButtonText = font.render("start", True, WHITE)
meditationBreathe = font.render("breathe in slowly...", True, BLACK)
meditationHold = font.render("hold...", True, BLACK)
meditationExhale = font.render("breathe out slowly...", True, BLACK)

#variables used for the meditation module
meditationTimestamp = pygame.time.get_ticks()
meditationStart = False
holdBreathing = False 
inhale = True 
exhale = False

size = 50 #default size is 50, passed into the meditation function call
targetInhaleSize = 200
targetExhaleSize = 50
targetSize = targetInhaleSize
inhaleTime = 5000
exhaleTime = 7000
holdBreathingTime = 2000
change = 0

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
    elif scene == 2: # meditation
        for event in pygame.event.get():
            print("hello")
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked
                if meditationButton1.collidepoint(event.pos):
                    meditationStart = True
                    print("hit")

        if(not meditationStart):
            med.drawMeditation(screen, size, change) #draw our meditation circle
            screen.blit(meditationWelcome1, (275, 50))
            screen.blit(meditationWelcome2, (10, 470))
            pygame.draw.rect(screen, BLACK, meditationButton1)
            screen.blit(meditationStartButtonText, (363, 528))
        else:
            med.drawMeditation(screen, size, change) #draw our meditation circle
            if(not holdBreathing):
                if(inhale):
                    change = med.calculateSizeGrow(meditationTimestamp,targetInhaleSize,inhaleTime)
                    if(med.checkTimestamp(meditationTimestamp, inhaleTime)):
                        holdBreathing = True
                        meditationTimestamp=pygame.time.get_ticks()
                elif(exhale):
                    change = med.calculateSizeShrink(meditationTimestamp,targetInhaleSize,exhaleTime,)
                    if(med.checkTimestamp(meditationTimestamp, exhaleTime)):
                        holdBreathing = True
                        meditationTimestamp=pygame.time.get_ticks()
            else:
                if(med.checkTimestamp(meditationTimestamp, holdBreathingTime)):
                    holdBreathing = False
                    meditationTimestamp=pygame.time.get_ticks()
                    if(inhale):
                        exhale = True
                        inhale = False
                    elif(exhale):
                        exhale = False
                        inhale = True
    elif scene == 3: # maze
        scene = maze.graphics(event, screen, font)
    elif scene == 4: # maze finish screen
        maze.done(screen, font)

    # Update the display
    pygame.display.flip()

