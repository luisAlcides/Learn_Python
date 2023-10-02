import pygame, sys, random
from pygame.locals import *

from Ball import *
from SimpleText import *
from SimpleButton import *


# Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 

# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Initialize variables
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
frameCountLabel = SimpleText(window, (60, 20), 'Program has run through this many loops: ', WHITE)
frameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
restartButton = SimpleButton(window, (280, 60), 'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        if restartButton.handleEvent(event):
            frameCounter = 0 # clicked button, reset counter
            
        
    # Do any per frame actions
    ball.update() # tell the ball to update itself
    frameCounter += 1 # increment each frame
    frameCountDisplay.setValue(str(frameCounter))
    
    # Clear the window before drawing it again
    window.fill(BLACK)
    
    # Draw the window elements
    ball.draw() # tell the ball to draw itself
    frameCountLabel.draw()
    frameCountDisplay.draw()
    restartButton.draw()
    
    # update the window
    pygame.display.update()
    
    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
            