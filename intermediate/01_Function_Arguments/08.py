my_num_list = [3, 6, 9]
numbers = {'num1': 3, 'num2': 6, 'num3': 9}


def sum1(num1, num2, num3):
    print(num1 + num2 + num3)


def sum2(num1, num2, num3):
    print(num1 + num2 + num3)


sum1(*my_num_list)
sum2(**numbers)

start_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values))

# unpacking parts of a iterable
a, *b, c = [3, 6, 9, 12, 15]
print('\n Unpacking parts of a iterable')
print(b)

# Merging iterables
print('\n Merging iterables')
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)

# Combining unpacking and packing
print('\n Combining unpacking and packing')
num_collection = [3, 6, 9]


def power_two(*nums):
    for num in nums:
        print(num**2)


power_two(*num_collection)