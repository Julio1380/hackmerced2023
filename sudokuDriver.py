import sudokuTable
import pygame
import sys
#background rect should be 515 size

def runSudoku(screen): 
    squareSize = 55
    selectX = 0
    selectY = 0

    #print the table
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        