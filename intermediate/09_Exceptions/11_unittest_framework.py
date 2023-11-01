# Importing unittest framework
import unittest


# Function that gets tested
def times_ten(number):
    return number * 100


# Test class
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')


# Practice

def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


class NearestExitTests(unittest.TestCase):

    def test_row_1(self):
        self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


unittest.main(argv=['first-arg-is-ignored'], exit=False)
