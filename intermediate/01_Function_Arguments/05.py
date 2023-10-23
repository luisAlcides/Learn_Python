# Working with **kwargs
def print_data(**data):
    for arg in data.values():
        print(arg)


def print_data2(postional_arg, **data):
    print(postional_arg)
    for arg in data.values():
        print(arg)


print_data(a='arg1', b=True, c=100)
print()
print('Print data 2')
print_data2('Position 1', a='arg1', b=True, c=100)

print()
print('Practice')

tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes'
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}


assign_table(2, 'Douglas', True)
print('-- tables with douglas -- \n', tables)


def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks


print('\n -- tables after update -- \n')
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)