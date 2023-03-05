import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

backbutton = pygame.Rect(0, 0, 75, 75)
block = pygame.Rect(0, 260, 25, 25)

# maze rectangles
maze1 = pygame.Rect(0, 225, 75, 25)
maze2 = pygame.Rect(0, 300, 75, 25)
maze3 = pygame.Rect(75, 75, 25, 175)
maze4 = pygame.Rect(75, 300, 25, 275)
maze5 = pygame.Rect(100, 75, 625, 25)
maze6 = pygame.Rect(100, 550, 625, 25)
maze7 = pygame.Rect(725, 75, 25, 100)
maze8 = pygame.Rect(725, 225, 25, 350)
maze9 = pygame.Rect(100, 400, 100, 25)
maze10 = pygame.Rect(575, 100, 25, 75)
maze11 = pygame.Rect(650, 150, 75, 25)
maze12 = pygame.Rect(600, 475, 125, 25)
maze13 = pygame.Rect(675, 225, 50, 25)
maze14 = pygame.Rect(650, 225, 25, 175)
maze15 = pygame.Rect(550, 400, 125, 25)
maze16 = pygame.Rect(525, 350, 25, 125)
maze17 = pygame.Rect(525, 300, 75, 50)
maze18 = pygame.Rect(575, 225, 25, 75)
maze19 = pygame.Rect(400, 475, 150, 25)
maze20 = pygame.Rect(400, 425, 25, 50)
maze21 = pygame.Rect(400, 400, 75, 25)
maze22 = pygame.Rect(450, 250, 25, 150)
maze23 = pygame.Rect(450, 225, 75, 25)
maze24 = pygame.Rect(150, 150, 25, 200)
maze25 = pygame.Rect(175, 250, 125, 25)
maze26 = pygame.Rect(300, 225, 25, 50)
maze27 = pygame.Rect(225, 150, 25, 50)
maze28 = pygame.Rect(250, 150, 275, 25)
maze29 = pygame.Rect(375, 175, 25, 150)
maze30 = pygame.Rect(250, 325, 150, 25)
maze31 = pygame.Rect(250, 350, 25, 125)
maze32 = pygame.Rect(150, 475, 200, 25)
maze33 = pygame.Rect(325, 400, 25, 75)

mazeWalls = [
    maze1, maze2, maze3, maze4, maze5, maze6, maze7, maze8, maze9, maze10,
    maze11, maze12, maze13, maze14, maze15, maze16, maze17, maze18, maze19, maze20,
    maze21, maze22, maze23, maze24, maze25, maze26, maze27, maze28, maze29, maze30,
    maze31, maze32, maze33
]

finishLine = pygame.Rect(750, 175, 50, 50)

# buildMaze is only used in the maze file
# DO NOT USE IN MAIN
# buildMaze gets rid of the ugly boilerplate code in the graphics function
def buildMaze(screen):
    for wall in mazeWalls:
        pygame.draw.rect(screen, BLACK, wall)

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

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        velocity[0] = 5
    if keys_pressed[pygame.K_LEFT]:
        velocity[0] = -5
    if keys_pressed[pygame.K_UP]:
        velocity[1] = -5
    if keys_pressed[pygame.K_DOWN]:
        velocity[1] = 5

    collided = 0

    for wall in mazeWalls:
        if wall.x - 25 < block.x + velocity[0] < wall.x + wall.width and wall.y - 25 < block.y + velocity[1] < wall.y + wall.height:
            collided += 1
            break
    if collided == 0:
        if block.x + velocity[0] >= 0 and block.x + velocity[0] <= 800 - 25:
            block.x += velocity[0]
        if block.y + velocity[1] >= 0 and block.y + velocity[1] <= 600 - 25:
            block.y += velocity[1]
    
    if finishLine.x - 25 < block.x + velocity[0] < finishLine.x + finishLine.width and finishLine.y - 25 < block.y + velocity[1] < finishLine.y + finishLine.height:
        return 4

    # render graphics
    screen.fill(WHITE)
    screen.blit(backarrow, (10, 10))
    buildMaze(screen)
    drawCharacter(screen)
    return 3

def doneLogic(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a button was clicked
        if backbutton.collidepoint(event.pos):
            return 0
    return 4

def done(screen, font):
    # variables needing screen or font
    backarrow = font.render("<-", True, BLACK)
    text = font.render("You win!", True, BLACK)

    screen.fill(WHITE)
    screen.blit(backarrow, (10, 10))
