# Fraction class
import math


class Fraction:

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, ' must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator ', denominator, ' must be an integer')
        self.numerator = numerator
        self.denominator = denominator

        # Use the math package to find the greatest common divisor
        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator = self.numerator // greatestCommonDivisor
            self.denominator = self.denominator // greatestCommonDivisor
        self.value = self.numerator / self.denominator
        # Normalize the sign of the numerator and denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        """Create a string representation of the fraction"""
        output = f'Fraction: {str(self.numerator)}/{str(self.denominator)} \nValue: {str(self.value)}'
        return output

    def __add__(self, otherFraction):
        """ Add two fraction objects """
        if not isinstance(otherFraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')

        # Use the math package to find the least common multiple
        newDenominator = math.lcm(self.denominator, otherFraction.denominator)
        multiplicationFactor = newDenominator // self.denominator
        equivalentNumerator = self.numerator * multiplicationFactor
        otherMultiplicationFactor = newDenominator // otherFraction.denominator
        otherFractionEquivalentNumerator = otherFraction.numerator * otherMultiplicationFactor
        newNumerator = equivalentNumerator + otherFractionEquivalentNumerator
        addedFraction = Fraction(newNumerator, newNumerator)
        return addedFraction

    def __eq__(self, otherFraction):
        """Test for equality"""
        if not isinstance(otherFraction, Fraction):
            return False  # not comparing to a fraction
        if (self.numerator == otherFraction.numerator) and (self.denominator == otherFraction.denominator):
            return True
        else:
            return False