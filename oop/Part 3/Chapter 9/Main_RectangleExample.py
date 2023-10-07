import pygame
import sys
from pygame.locals import *
from Rectangle import *

# Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Set up window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectanglesList = []
for i in range(N_RECTANGLES):
    rectangle = Rectangle(window)
    rectanglesList.append(rectangle)

whichRectangle = FIRST_RECTANGLE

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONUP:
            for rectangle in rectanglesList:
                if rectangle.clickedInside(event.pos):
                    print('Clicked on', whichRectangle, ' rectangle.')

                    if whichRectangle == FIRST_RECTANGLE:
                        firstRectangle = rectangle
                        whichRectangle = SECOND_RECTANGLE
                    elif whichRectangle == SECOND_RECTANGLE:
                        secondRectangle = rectangle
                        # User has chosen 2 rectangles, let's compare
                        if firstRectangle == secondRectangle:
                            print('Rectangle are the same size')
                        elif firstRectangle < secondRectangle:
                            print('First rectangle is smaller than second rectangle.')
                        else: # must be larger
                            print('First rectangle is larger than second rectangle.')
                            whichRectangle = FIRST_RECTANGLE

        # Clear the window and draw all rectangles
        window.fill(WHITE)
        for rectangle in rectanglesList:
            rectangle.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
