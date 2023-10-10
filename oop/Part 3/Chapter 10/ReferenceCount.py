# Reference count example
import sys


class Square:
    def __init__(self, width, color):
        self.width = width
        self.color = color


# Instantiate an object
square1 = Square(10, 'red')
print(square1)
# Reference count of the Square object is 1
# Now set another variable to the same object

square2 = square1
print(square2)
# Reference count of the Square object is 2

print('Reference count is', sys.getrefcount(square1))
