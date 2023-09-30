# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
from pathlib import Path
import sys

# 2 - Define constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pathToBall = BASE_PATH.joinpath('images', 'ball.png')


# 4 - Load assets: image(s), sounds,  etc.
ballImage = pygame.image.load('images/ball.png')

# 5 - Initialize variables


# 6 - Loop forever

while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 8 - Do any "per frame" actions
    
    # 9 - Clear the screen
    window.fill(BLACK)
    
    # 10 - Draw all window elements
    window.blit(ballImage, (100,200))
    
    
    # 11 - Update the screen
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)