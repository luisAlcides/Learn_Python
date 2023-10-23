# nonlocal
def enclosing_function():
    var = 'value'

    def nested_function():
        nonlocal var
        var = 'new_value'

    nested_function()
    print(var)


enclosing_function()

print()
print('Practice')

walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):
    square_feet = 0

    def calc_square_feet():
        for width, height in wall_measurements:
            nonlocal square_feet
            square_feet += width * height

    calc_square_feet()
    
    def calc_gallons():
        return square_feet / 400

    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))