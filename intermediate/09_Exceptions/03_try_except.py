# Try / Except
colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}

for color in ('red', 'green', 'yellow'):
    try:
        print('The hex value of ' + color + ' is ' + colors[color])
    except:
        print('An exception occurred! Color does not exist')
        print('Loop continues')

# Practice
print()
print()
staff = {
    'Austin': {
        'floor managers': 1,
        'sales associates': 5
    },
    'Melbourne': {
        'floor managers': 0,
        'sales associates': 8
    },
    'Beijing': {
        'floor managers': 2,
        'sales associates': 5
    },
}


def print_staff_report(location, staff_dict):
    managers = staff_dict['floor managers']
    sales_people = staff_dict['sales associates']
    ratio = sales_people / managers
    print('Instrument world ' + location + ' has:')
    print(str(sales_people) + ' sales employees')
    print(str(managers) + ' floors managers')
    print('The ratio of sales people to managers is ' + str(ratio))
    print()


for location, staff in staff.items():
    try:
        print_staff_report(location, staff)
    except:
        print('Could not print sales report for ' + location)
