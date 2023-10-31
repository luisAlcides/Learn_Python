# user-defined custom exceptions

class LocationTooFarError(Exception):
    pass


def schedule_delivery(distance_from_store):
    if distance_from_store > 10:
        raise LocationTooFarError
    else:
        print('Scheduling the delivery...')


# schedule_delivery(11)


# Practice
print('\n--------------------Practice--------------------------------------\n')

inventory = {
    'Piano': 3,
    'Lute': 1,
    'Sitar': 2
}


class InventoryError(Exception):
    pass


def submit_order(instrument, quantity):
    supply = inventory[instrument]

    if quantity > supply:
        raise InventoryError
    else:
        inventory[instrument] -= quantity
        print('Successfully place order! Remaining supply: ' + str(inventory[instrument]))


instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
