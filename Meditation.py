import pygame
import sys
import time

button4 = pygame.Rect(325, 480, 150, 50)
    
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

text = 10

#change = 0

#simple
def drawMeditation(screen, size, change):
        #Testing = main.font.render(str(pygame.time.get_ticks()), True, main.WHITE) display milliseconds
        screen.fill(WHITE)
        #draw circle
        pygame.draw.circle(screen, (3,252,177), (400,280), size + change)

def checkTimestamp(timestamp, millis):
       if(pygame.time.get_ticks() - timestamp > millis):
              return True
       else:
              return False
       
def calculateSizeGrow(timestamp,targetSize,targetTime):
       difference = pygame.time.get_ticks() - timestamp
       return difference/(targetTime/(targetSize))

#if we are shrinking, we can assume we started shrinking from our max size
def calculateSizeShrink(timestamp,maxSize,targetTime,):
       difference = pygame.time.get_ticks() - timestamp
       return maxSize - difference/(targetTime/(maxSize))



       

