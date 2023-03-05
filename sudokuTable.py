import pygame

class Square:
    def __init__(self, value, x, y, size):
        self.size = size
        self.x1 = x
        self.y1 = y
        self.x2 = x + size
        self.y2 = y + size  
        self.value = value
        self.tile = pygame.Rect(x, y, size, size)

class sudoku:
    def __init__(self):
        self.table = [[0,0,3,0,5,4,0,6,1],
                      [0,0,1,7,0,0,0,0,2],
                      [0,0,0,0,0,0,7,8,0],
                      [0,0,0,0,0,5,0,0,0],
                      [3,6,4,9,2,0,0,0,0],
                      [0,2,0,0,0,6,0,0,0],
                      [0,8,0,4,0,1,2,7,0],
                      [0,3,2,6,0,7,8,4,5],
                      [4,9,7,0,0,0,3,0,0]]
        
        self.solution = [[2,7,3,8,5,4,9,6,1],
                         [8,4,1,7,6,9,5,3,2],
                         [9,5,6,2,1,3,7,8,4],
                         [7,1,9,3,4,5,6,2,8],
                         [3,6,4,9,2,8,1,5,7],
                         [5,2,8,1,7,6,4,9,3],
                         [6,8,5,4,3,1,2,7,9],
                         [1,3,2,6,9,7,8,4,5],
                         [4,9,7,5,8,2,3,1,6]]
        
        self.color = [[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]
        
    def setValue(self, x, y, value):
        self.table[x][y] = value;

    def getValue(self, x, y, value):
        return self.table[x][y]
    

    def checkValue(self, x, y):
        if self.table[x][y] == self.solution[x][y]:
            return True
        return False
    