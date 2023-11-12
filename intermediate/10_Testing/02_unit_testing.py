# unit test

# The unit we want to test
def times_ten(number):
    return number * 10


# A unit test function with a single test case
def test_multiply_ten_by_zero():
    assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'


def test_multiply_ten_by_one_million():
    assert times_ten(1000000) == 1000000, 'Expected times_ten(1000000) to return 1000000'


def test_multiply_ten_negative_number():
    assert times_ten(-10) == -100, 'Expected times_ten(-10) to return -100'


# Practice
def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


def test_row_1():
    assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'


def test_row_20():
    assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'


def test_row_40():
    assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back'


test_row_1()
test_row_20()
test_row_40()
print()
