import pygame, sys, random
from pygame.locals import *
from Ball import *


# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30 

# Initialize variables
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initizalize variables
ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Main game loop
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Do any per frame actions
    ball.update()
    
    # Clear the window before drawing it again
    window.fill(BLACK)
    
    # Draw the window elements
    ball.draw() # tell the ball to draw itself
    
    # update the window
    pygame.display.update()
    
    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)