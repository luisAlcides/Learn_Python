from asyncio import events
import pygame
import sys
import random
from pygame.locals import *
from SimpleButton import *

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

button = SimpleButton(window, (100, 100), 'images/buttonUp.png', 'images/buttonDown.png')
buttonB = SimpleButton(window, (300, 100), 'images/buttonUp.png', 'images/buttonDown.png')
buttonC = SimpleButton(window, (450, 100), 'images/buttonUp.png', 'images/buttonDown.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

        if button.handleEvent(event):
            print('User has clicked the button')
            
        
        if buttonB.handleEvent(event):
            print('User has clicked the buttonB')
        
        
        if buttonC.handleEvent(event):
            print('User has clicked the buttonC')
    
    window.fill(BLACK)

    button.draw()
    buttonB.draw()
    buttonC.draw()
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)