import pygame
import sys
import Meditation

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG = WHITE

# Scene is to know what scene to show
scene = 0

# Define some fonts
font = pygame.font.SysFont(None, 48)

# Define some text
text0 = font.render("Click a button to change the screen", True, BLACK)
text1 = font.render("Welcome to scene 1", True, BLACK)
text2 = font.render("Welcome to scene 2", True, WHITE)

# Define some buttons
button1 = pygame.Rect(200, 250, 150, 50)
button2 = pygame.Rect(450, 250, 150, 50)

# Define some button text
button1_text = font.render("Black", True, WHITE)
button2_text = font.render("White", True, WHITE)
button3_text = font.render("Back", True, BLACK)
button4_text = font.render("Back", True, WHITE)

#variables used for the meditation module
meditationTimestamp = pygame.time.get_ticks()
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

# Set up the game loop
while True:
    #clock = pygame.time.get_ticks()
    #Testing = font.render(str(clock), True, WHITE)
    # Handle events
    for event in pygame.event.get():
        if scene == 0:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if a button was clicked
                    if button1.collidepoint(event.pos):
                        scene = 1
                    elif button2.collidepoint(event.pos):
                        scene = 2
        elif scene == 1:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked
                if button1.collidepoint(event.pos):
                    scene = 0
        elif scene == 2:
            Meditation.meditation(event)

    # Draw the menu
    if scene == 0:
        screen.fill(BG)
        pygame.draw.rect(screen, BLACK, button1)
        pygame.draw.rect(screen, BLACK, button2)
        screen.blit(text0, (200, 200))
        screen.blit(button1_text, (215, 260))
        screen.blit(button2_text, (470, 260))
    elif scene == 1:
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, button1)
        screen.blit(text1, (200, 200))
        screen.blit(button3_text, (215, 260))
    elif scene == 2:
        Meditation.drawMeditation(size, change)

        if(not holdBreathing):
            if(inhale):
                change = Meditation.calculateSizeGrow(meditationTimestamp,targetInhaleSize,inhaleTime)
                if(Meditation.checkTimestamp(meditationTimestamp, inhaleTime)):
                    holdBreathing = True
                    meditationTimestamp=pygame.time.get_ticks()
            elif(exhale):
                change = Meditation.calculateSizeShrink(meditationTimestamp,targetInhaleSize,exhaleTime,)
                if(Meditation.checkTimestamp(meditationTimestamp, exhaleTime)):
                    holdBreathing = True
                    meditationTimestamp=pygame.time.get_ticks()
        else:
            if(Meditation.checkTimestamp(meditationTimestamp, holdBreathingTime)):
                holdBreathing = False
                meditationTimestamp=pygame.time.get_ticks()
                if(inhale):
                    exhale = True
                    inhale = False
                elif(exhale):
                    exhale = False
                    inhale = True
                    



    # Update the display
    pygame.display.flip()

