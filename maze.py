import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

backbutton = pygame.Rect(0, 0, 75, 75)

def logic(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a button was clicked
        if backbutton.collidepoint(event.pos):
            return 0
    return 3

def graphics(screen, font):
    # variables needing screen or font
    backarrow = font.render("<-", True, BLACK)

    # render graphics
    screen.fill(WHITE)
    screen.blit(backarrow, (10, 10))