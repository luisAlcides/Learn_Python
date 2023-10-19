# Triangle class
import pygame
import random
from ShapeBasic import *

# Set up the colrs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Triangle(Shape):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Triangle', maxWidth, maxHeight)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangleSlope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False

        # Do some math to see if the point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = mousePoint[1] - self.y
        if xOffset == 0:
            return True

        # Calculate the slope (rise over run)
        pointSlopeFromYIntercept = (yOffset - self.height) / xOffset

        if pointSlopeFromYIntercept < self.triangleSlope:
            return True
        else:
            return False

    def getType(self):
        return self.shapeType

    def getArea(self):
        theArea = .5 * self.width * self.maxHeight
        return theArea

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            (
                                (self.x, self.y + self.height),
                                (self.x, self.y),
                                (self.x + self.width, self.y)
                            )
                            )