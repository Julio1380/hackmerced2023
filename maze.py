import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

backbutton = pygame.Rect(0, 0, 75, 75)
characterHitBox = pygame.Rect(0, 260, 25, 25)

velocity = [0, 0]

# buildMaze is only used in the maze file
# DO NOT USE IN MAIN
# buildMaze gets rid of the ugly boilerplate code in the graphics function
def buildMaze():
    pass

# drawCharacter is only used in the maze file
# DO NOT USE IN MAIN
# drawCharacter gets rid of the ugly biolerplate code in the graphics function
def drawCharacter(screen):
    pygame.draw.rect(screen, BLACK, characterHitBox)

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
    buildMaze()
    drawCharacter(screen)
