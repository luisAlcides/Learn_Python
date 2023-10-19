# Variable number of arguments: **kwargs

def arbitrary_keyword_args(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # see if there's 'anything_goes' keyword arg and print it
    print(kwargs.get('anything_goes'))


arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)

# Practice
print('\n\n')
print('Practice\n')

tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order':{
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes'
        },
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

print(tables)


def assign_food_items(**order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    print(order_items)
    print(food, drinks)


assign_food_items(food='Pancakes, Poached Egg', drinks='Water')
