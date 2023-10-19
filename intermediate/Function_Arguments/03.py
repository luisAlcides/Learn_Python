# Working with *args

def shout_string(*args):
    for argument in args:
        print(argument.upper())


def truncate_sentences(length, *sentences):
    for sentence in sentences:
        print(sentence[:length])


shout_string('working on', 'learning', 'argument unpacking!')
truncate_sentences(8, 'What\'s going on here', 'Looks like we\'ve been cut off')


tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}
print()
print(tables)
print()


def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''


def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for item in order_items:
        print(item)


assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)