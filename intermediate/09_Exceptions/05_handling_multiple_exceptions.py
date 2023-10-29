# Handling Multiple Exceptions

try:
    print(somevariables)
except (NameError, ZeroDivisionError) as e:
    print('We hit an Exception!')
    print(e)

print()
try:
    print(s)
except NameError:
    print('We hit a NameError Exception!')
except KeyError:
    print('We hit a TyperError Exception!')
except Exception:
    print('We hit an exception that is not a NameError or TypeError!')


# Practice ---------------------------------------------------------------
print()
print('Practice-----------------------------------------------------------')
print()
instrument_prices = {
    'Banjo': 200,
    'Cello': 1000,
    'Flute': 100,
}


def display_discounted_price(instrument, discount):
    full_price = instrument_prices[instrument]
    discount_percentage = discount / 100
    discount_price = full_price - (full_price * discount_percentage)
    print('The instrument\' discounted price is: ' + str(discount_price))


instrument = 'Banjo'
discount = '20'
try:
    display_discounted_price(instrument, discount)
except KeyError:
    print('An invalid instrument was entered!')
except TypeError:
    print('Discount percentage must be a number!')
except Exception:
    print('Hit an exception other than KeyError or TypeError!')