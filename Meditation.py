import pygame
import sys
import main
import time


button4 = pygame.Rect(325, 480, 150, 50)

def meditation(event):
    if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button was clicked
                if button4.collidepoint(event.pos):
                    main.scene = 0
    
    #main.screen.fill(main.WHITE)
    #pygame.draw.circle(main.screen, (0,0,255), (250,250), 75)
    #pygame.draw.lines(main.screen, (0,0,255), True, [(0,100), (100, 200)])
    #pygame.display.update()


text = 10

#change = 0

#simple
def drawMeditation(size, change):
        #Testing = main.font.render(str(pygame.time.get_ticks()), True, main.WHITE) display milliseconds
        main.screen.fill(main.WHITE)
        #draw circle
        pygame.draw.circle(main.screen, (3,252,177), (400,280), size + change)

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



       

