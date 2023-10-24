# Here, we assign a function to a variable
uppercase = str.upper

# And the call it
big_pie = uppercase('pumpkinpie')

# Here we store two functions in a list
string_manipulation_functions = [str.upper, str.lower]


# Functions as arguments
def total_bill(func, value):
    total = func(value)
    return 'The total amount owed is $' + '{:.2f}'.format(total) + '. Thank you! :)'


def add_tax(total):
    tax = total * 0.06
    new_total = total + tax
    return new_total


def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total


tax = total_bill(add_tax, 100)
tip = total_bill(add_tip, 100)
print('tax: ', tax)
print('tip: ', tip)

# Functions as Arguments-iteration
print()
print('Functions as arguments-iteration')
bills = [115, 120, 42]
new_bills = []

for i in range(len(bills)):
    total = add_tax(bills[i])
    new_bills.append('Total amount owed is $' + '{:.2f}'.format(total) + '. Thank you :)')

print(new_bills)


def total_bills2(func, list):
    # This list will store all the new bill values
    new_bills = []

    # This loop will iterate through our bills
    for i in range(len(list)):
        # Here we apply the function to each element of the list!
        total = func(list[i])
        new_bills.append('Total amount owed is $' + '{:.2f}'.format(total) + '. Thank you! :)')
    return new_bills


bills_w_tax = total_bills2(add_tax, bills)
print('bills_w_tax: ', bills_w_tax)

# Functions as Return values
print()
print('Functios as return values')


def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,
    # length & width, and returns the volume given the input height
    def volume(length, width):
        return length * width * height

    return volume


box_volume_height15 = make_box_volume_function(15)
print('box_volume_height15: ', box_volume_height15(3, 2))