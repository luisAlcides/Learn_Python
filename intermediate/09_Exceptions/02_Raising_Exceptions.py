# Raising Exceptions

# raise NameError
# raise NameError('Custom Message')

def open_register(employee_status):
    if employee_status == 'Authorized':
        print('Successfully opened cash register')
    else:
        # Alternativees: raise TypeError() or TypeError('Message')
        raise Exception('Employee does not have access!')


# open_register('not Authorized')

# Practice

instrument_catalog = {
    'Marimba': 1999,
    'Kora': 499,
    'Flute': 899
}


def print_instrument_price(instrument):
    if instrument in instrument_catalog:
        print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    else:
        raise KeyError(f'{instrument} is not found in instrument catalog!')


print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')
