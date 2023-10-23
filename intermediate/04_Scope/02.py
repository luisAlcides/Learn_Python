# Enclosing scope
def function_outer():
    variable_exterior = 42

    def function_inner():
        nonlocal variable_exterior
        variable_exterior = 10

    function_inner()
    print(variable_exterior)


function_outer()
print('\n Enclosing')


def outer_function():
    enclosing_value = 'Enclosing Value'

    def nested_function():
        nested_value = 'Nested Value'

        def second_nested():
            print(enclosing_value)
            print(nested_value)

        second_nested()

    nested_function()


outer_function()

print()
print('Practice')


def calc_paint_amount(width, height):

    square_feet = width * height

    def calc_gallons():
        return square_feet / 400

    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30, 20)))
