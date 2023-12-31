# Rectangle class
import pygame
import random
from ShapeBasic import *

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Rectangle(Shape):

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        super().__init__(window, shapeType, maxWidth, maxHeight)
        self.width = random.choice((20, 30, 40))
        self.height = random.choice((20, 30, 40))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.area = self.width * self.height

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    # Magic method called when you compare
    # two Rectangle objects using the == operator
    def __eq__(self, otherRectangle):
        if not isinstance(otherRectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')
        if self.area == otherRectangle.area:
            return True
        else:
            return False

    # Magic method called when you compare
    # two Rectangle objects with the < operator
    def __lt__(self, otherRectangle):
        if not isinstance(otherRectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')

        if self.area < otherRectangle.area:
            return True
        else:
            return False

    # Magic method called when you compare
    # two Rectangle objects with the > operator
    def __gt__(self, otherRectangle):
        if not isinstance(otherRectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')

        if self.area > otherRectangle.area:
            return True
        else:
            return False

    def getArea(self):
        return self.area

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
