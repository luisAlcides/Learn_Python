# Variable number of arguments: *args

def my_function(*args):
    print(args)


my_function('Args', 245, False)


def print_order(*order_items):
    print(order_items)


print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')