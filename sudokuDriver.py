import sudokuTable as st
import pygame
import sys
#background rect should be 515 size

WHITE = (255,255,255)
BLACK = (0,0,0)
SQUARE_SIZE = 55
TABLE_LEFT_BUFFER = 142.5
TABLE_UP_BUFFER = 42.5

backbutton = pygame.Rect(0, 0, 75, 75)
selectX = 0
selectY = 0

def runSudoku(event, sudoku): 
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if a button was clicked
        if backbutton.collidepoint(event.pos):
            return 0
        if event.pos[0] < TABLE_LEFT_BUFFER or event.pos[0] > (800 - TABLE_LEFT_BUFFER) or event.pos[1] < TABLE_UP_BUFFER or event.pos[1] > (800 - TABLE_UP_BUFFER):
            return
        selectX = int((event.pos[0] - TABLE_LEFT_BUFFER)/57)
        selectY = int((event.pos[1] - TABLE_UP_BUFFER)/57)
    
    elif event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            value = 1
        elif event.key == pygame.K_2:
            value = 2            
        elif event.key == pygame.K_3:
            value = 3
        elif event.key == pygame.K_4:
            value = 4
        elif event.key == pygame.K_5:
            value = 5
        elif event.key == pygame.K_6:
            value = 6
        elif event.key == pygame.K_7:
            value = 7
        elif event.key == pygame.K_8:
            value = 8
        elif event.key == pygame.K_9:
            value = 9
        else:
            return
        sudoku.setValue(selectX, selectY,value)
        if not sudoku.checkValue(selectX, selectY):
            sudoku.color[selectX][selectY] = 1
    
    return 1


    

def printSudoku(screen, sudoku):
    screen.fill(WHITE)
    squares = [[st.Square(sudoku.table[i][j], TABLE_LEFT_BUFFER + 2 + i *(SQUARE_SIZE + 2), TABLE_UP_BUFFER + 2 + j *(SQUARE_SIZE + 2), SQUARE_SIZE) for j in range(9)] for i in range(9)]
    border = pygame.Rect(TABLE_LEFT_BUFFER, TABLE_UP_BUFFER, 515, 515)

    font = pygame.font.SysFont(None, 48)

    pygame.draw.rect(screen, BLACK, border)
    backarrow = font.render("<-", True, BLACK)
    screen.blit(backarrow, (10, 10))

    for i in range(9):
        for j in range(9):
            boxColor = WHITE
            if sudoku.color[i][j] == 1:
                boxColor = (128,0,0)
            pygame.draw.rect(screen, boxColor, squares[i][j].tile)
            num = font.render(str(squares[i][j].value), True, BLACK);
            numX = ((squares[i][j].x1 + squares[i][j].x2)/2) -10
            numY = ((squares[i][j].y1 + squares[i][j].y2)/2) -15
            screen.blit(num, (numX, numY))
        