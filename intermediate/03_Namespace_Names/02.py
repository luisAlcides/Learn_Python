# Global namespace

import random

first_name = 'Jaya'
last_name = 'Bodegard'


def print_variables(first_name, last_name):
    random_number = random.randint(0, 9)
    print(first_name)
    print(last_name)
    print(random_number)


print_variables(first_name, last_name)
print(globals())