# Parameterizing tests

import unittest


# The function we want to test
def times_ten(number):
    return number * 100


def divide(a, b):
    return a / b


class TestTimesTen(unittest.TestCase):

    # A test method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest(num):
                expected_result = num * 10
                message = f'Expected times_ten({str(num)}) to return {str(expected_result)}'
                self.assertEqual(times_ten(num), expected_result, message)


class TestDivision(unittest.TestCase):

    def test_divide_positive_numbers(self):
        test_cases = [
            (10, 2, 5),
            (15, 3, 5),
            (8, 4, 2)
        ]

        for case in test_cases:
            with self.subTest(case):
                a, b, expected_result = case
                result = divide(a, b)
                self.assertEqual(result, expected_result)

    def test_divide_by_zero(self):
        with self.subTest(msg='Testing division by zero'):
            with self.assertRaises(ZeroDivisionError):
                divide(10, 0)
