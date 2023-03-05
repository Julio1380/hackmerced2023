import pygame
import sys
import time

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

# Set up the game loop
while True:

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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked
                if button1.collidepoint(event.pos):
                    scene = 0

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
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, button1)
        screen.blit(text2, (200, 200))
        screen.blit(button4_text, (215, 260))

    # Update the display
    pygame.display.flip()
