import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

backbutton = pygame.Rect(0, 0, 75, 75)
block = pygame.Rect(0, 260, 25, 25)

# buildMaze is only used in the maze file
# DO NOT USE IN MAIN
# buildMaze gets rid of the ugly boilerplate code in the graphics function
def buildMaze():
    pass

# drawCharacter is only used in the maze file
# DO NOT USE IN MAIN
# drawCharacter gets rid of the ugly biolerplate code in the graphics function
def drawCharacter(screen):
    pygame.draw.rect(screen, BLACK, block)

def logic(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a button was clicked
        if backbutton.collidepoint(event.pos):
            return 0
    return 3

def graphics(event, screen, font):
    # variables needing screen or font
    backarrow = font.render("<-", True, BLACK)

    #extra logic
    velocity = [0, 0]

    keys_pressed =pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        velocity[0] = 10
    if keys_pressed[pygame.K_LEFT]:
        velocity[0] = -10
    if keys_pressed[pygame.K_UP]:
        velocity[1] = -10
    if keys_pressed[pygame.K_DOWN]:
        velocity[1] = 10
    block.x += velocity[0]
    block.y += velocity[1]

    # render graphics
    screen.fill(WHITE)
    screen.blit(backarrow, (10, 10))
    buildMaze()
    drawCharacter(screen)
