# Local Namespace

global_variable = 'global'


def add(num1, num2):
    nested_value = 'Inside Function'
    print(num1 + num2)
    print(locals())


add(5, 10)

# Practice
print(locals())
print(globals())


def divide(num1, num2):
    result = num1 / num2
    print(result)
    print(locals())


def multiply(num1, num2):
    product = num1 * num2
    print(product)
    print(locals())


divide(3, 4)
multiply(4, 50)
print(locals())