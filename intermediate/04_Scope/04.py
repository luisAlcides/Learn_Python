# global scope
gravity = 9.8


def get_force(mass):
    global gravity
    gravity += 100
    return mass * gravity


print(get_force(60))

print()
print('Practice')
paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}


def print_available(color):
    print('There are ' + str(paint_gallons_available[color]) + ' gallons available of '
          + color + ' paint.')


def print_all_colors_available():
    for color in paint_gallons_available:
        print(color)


print_available('red')
print_all_colors_available()
