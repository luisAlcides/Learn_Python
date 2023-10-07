# Test code
from Fraction import *

fraction1 = Fraction(1, 3)
fraction2 = Fraction(2, 5)
print('Fraction1: ', fraction1)
print('Fraction 2: ', fraction2)

sumFraction = fraction1 + fraction2  # calls __add__
print('Sum is: ', sumFraction)

print('Are fractions 1 and 2 equal? ', (fraction1 == fraction2))  # expect False
print()

fraction3 = Fraction(-20, 80)
fraction4 = Fraction(4, -16)
print('Fraction 3: ', fraction3)
print('Fraction 4: ', fraction4)
print('Are fractions 3 and 4 equal?', (fraction3 == fraction4))  # expect True
print()

fraction5 = Fraction(5, 2)
fraction6 = Fraction(500, 200)
print('Sum of 5 / 2 and 500/2\n', fraction5+fraction6)

