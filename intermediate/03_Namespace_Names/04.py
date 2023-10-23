# Enclosing namespace

global_variable = 'global'


def outer_function():
    outer_value = 'outer'

    def inner_function():
        inner_value = 'inner'
        print(outer_value)

    inner_function()
    print(locals())


outer_function()
print()
print()
print('Different globals from locals')
print(globals())


def simple_math_func():
    x = 10
    y = 2
    mult = x * y
    add = x + y


print(locals())
