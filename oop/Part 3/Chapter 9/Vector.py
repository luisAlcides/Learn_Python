# Vector
import math


class Vector:
    """The Vector class represents two values as a vector, allows for manny math calculations"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # called for + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # called for - operator
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # called for * operator
        # Special code to allow for multiplying by a vector or a scalar
        if isinstance(other, Vector):  # Multiply two vectors
            return Vector((self.x * other.x), (self.y * other.y))
        elif isinstance(other, (int, float)):  # multiply by a scalar
            return Vector((self.x * other), (self.y * other))
        else:
            raise TypeError('Second value must be a vector or scalar')

    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, other):  # called for == operator
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # called for != operator
        return not (self == other)  # calls __eq__ method

    def __lt__(self, other):  # called for < operator
        if abs(self) < abs(other):  # calls __abs__ method
            return True
        else:
            return False

    def __gt__(self, other):  # called for > operator
        if abs(self) > abs(other):  # calls __abs__ method
            return True
        else:
            return False

    def __str__(self):
        return f'This vector has the value {str(self.x)}, {str(self.y)}'