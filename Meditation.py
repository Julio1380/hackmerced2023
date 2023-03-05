import pygame
import sys
import time

class Meditation:

       def __init__(self, inScreen, font):
              self.button4 = pygame.Rect(325, 480, 150, 50)

              # Define some colors
              self.WHITE = (255, 255, 255)
              self.BLACK = (0, 0, 0)
              self.PASTEL = (255, 202, 175)
              self.PURUPLE = (224, 187, 228)
              self.BG = (240, 220, 240)

              self.screen = inScreen
              self.font = font

              #define some button text
              self.meditationBackArrow = font.render("<-", True, self.BLACK)

              #define some text used for the meditation scene
              self.meditationWelcome1 = font.render("meditation time", True, self.BLACK)
              self.meditationWelcome2 = font.render("Deep breathing relaxes the body. Ready to start?", True, self.BLACK)
              self.meditationStartButtonText = font.render("start", True, self.WHITE)
              self.meditationBreathe = font.render("breathe in slowly...", True, self.BLACK)
              self.meditationHold = font.render("hold...", True, self.BLACK)
              self.meditationExhale = font.render("breathe out slowly...", True, self.BLACK)
              self.meditationAgain = self.font.render("again?", True, self.WHITE)
              self.meditationFinished = self.font.render("finished!", True, self.BLACK)

               # buttons used for meditation
              self.meditationStartButton = pygame.Rect(325, 520, 150, 50)
              self.meditationBackButton = pygame.Rect(0, 0, 75, 75)

              #variables used for the meditation module
              self.meditationTimestamp = pygame.time.get_ticks()
              self.meditationStart = False
              self.hold = False 
              self.inhale = True 
              self.exhale = False

              self.size = 50 #default size is 50, passed into the meditation function call
              self.sizeChange = 0
              self.targetInhaleSize = 200
              self.targetExhaleSize = 50
              self.targetSize = self.targetInhaleSize
              self.inhaleTime = 4500
              self.exhaleTime = 3500
              self.holdBreathingTime = 2500
              self.cycles = 0

       def reset(self):
              self.meditationTimestamp = pygame.time.get_ticks()
              self.meditationStart = False
              self.hold = False 
              self.inhale = True 
              self.exhale = False

              self.size = 50 #default size is 50, passed into the meditation function call
              self.sizeChange = 0
              self.targetInhaleSize = 200
              self.targetExhaleSize = 50
              self.targetSize = self.targetInhaleSize
              self.inhaleTime = 4500
              self.exhaleTime = 3500
              self.holdBreathingTime = 2500
              self.cycles = 0
              
       def draw(self):
              self.screen.fill(self.BG)
              self.screen.blit(self.meditationBackArrow, (10, 10)) # draw back arrow

              self.drawMeditation() #draw our meditation circle

              if(self.cycles >= 5):
                     self.screen.blit(self.meditationWelcome1, (330, 50))
                     self.screen.blit(self.meditationFinished, self.meditationFinished.get_rect(center=(800/2, 380))) # draw finished text
                     self.sizeChange = self.calculateSizeGrow(self.meditationTimestamp, 0.1, 500)
                     pygame.draw.rect(self.screen, self.BLACK, self.meditationStartButton)
                     self.screen.blit(self.meditationAgain, (374, 535))
                     return

              
              
              if(not self.meditationStart):
                     self.screen.blit(self.meditationWelcome1, (330, 50))
                     self.screen.blit(self.meditationWelcome2, (100, 480))
                     pygame.draw.rect(self.screen, self.BLACK, self.meditationStartButton)
                     self.screen.blit(self.meditationStartButtonText, (380, 535))
              else:
                     if(not self.hold):
                            if(self.inhale):
                                   self.screen.blit(self.meditationBreathe, self.meditationBreathe.get_rect(center=(800/2, 565)))
                                   self.sizeChange = self.calculateSizeGrow(self.meditationTimestamp,self.targetInhaleSize,self.inhaleTime)
                                   if(self.checkTimestamp(self.meditationTimestamp, self.inhaleTime)):
                                          self.hold = True
                                          self.meditationTimestamp=pygame.time.get_ticks()
                            elif(self.exhale):
                                   self.screen.blit(self.meditationExhale, self.meditationExhale.get_rect(center=(800/2, 565)))
                                   self.sizeChange = self.calculateSizeShrink(self.meditationTimestamp,self.targetInhaleSize,self.exhaleTime)
                                   if(self.checkTimestamp(self.meditationTimestamp, self.exhaleTime)):
                                          self.hold = True
                                          self.meditationTimestamp=pygame.time.get_ticks()
                                          self.cycles+=1
                     else:
                            self.screen.blit(self.meditationHold, self.meditationHold.get_rect(center=(800/2, 565)))
                            if(self.checkTimestamp(self.meditationTimestamp, self.holdBreathingTime)):
                                   self.hold = False
                                   self.meditationTimestamp=pygame.time.get_ticks()
                                   if(self.inhale):
                                          self.exhale = True
                                          self.inhale = False
                                   elif(self.exhale):
                                          self.exhale = False
                                          self.inhale = True
                                   
       def handleEvent(self, event):
              if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
              elif event.type == pygame.MOUSEBUTTONDOWN:
                     if self.meditationStartButton.collidepoint(event.pos):
                            self.reset()
                            self.meditationStart = True
                            return 2 
                     elif self.meditationBackButton.collidepoint(event.pos):
                            return 0 #exit button clicked, return to menu
              return 2 # else stay in current scene

       def drawMeditation(self):
              #draw circle
              pygame.draw.circle(self.screen, (3,252,177), (400,280), self.size + self.sizeChange)

       def checkTimestamp(self, timestamp, millis):
              if(pygame.time.get_ticks() - timestamp > millis):
                     return True
              else:
                     return False
              
       def calculateSizeGrow(self, timestamp,targetSize,targetTime):
              difference = pygame.time.get_ticks() - timestamp
              return difference/(targetTime/(targetSize))

       #if we are shrinking, we can assume we started shrinking from our max size
       def calculateSizeShrink(self, timestamp,maxSize,targetTime):
              difference = pygame.time.get_ticks() - timestamp
              return maxSize - difference/(targetTime/(maxSize))



              

