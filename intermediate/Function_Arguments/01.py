# Positional Arguments
def positional_arguments(first_name, last_name):
    print(first_name, last_name)


# Keyword Arguments

def keyword_arguments(first_name, last_name):
    print(first_name, last_name)


# Default Arguments
def default_arguments(first_name='Natalia', last_name='Gomez'):
    print(first_name, last_name)


print('Positional Arguments')
positional_arguments('Jiho', 'Baggins')
print()

print('Keyword Arguments')
keyword_arguments(first_name='Lau', last_name='Mauro')
print()

print('Default Arguments')
default_arguments()

"""
1.Our friend Jiho is trying to get into the restaurant business. 
They asked us to build a simple table assignment program to help manage which customer 
is assigned to each table in the restaurant. Jiho wants to store not only the name of 
the customer for the table but also if they hold a VIP status (earned by visiting the 
restaurant frequently).

Our table information will be stored in a dictionary called tables (already defined in 
our editor) that is structured in the following format:

tablenumber: [name, vip_status]
"""

# Ejercicio 1
table_number = []


def client(name, vip_status=False):
    table_number.append({name, vip_status})


client('Jiho', False)
client('Leonard', False)
client('Marco', True)
client('Mauro', False)


print(table_number)
