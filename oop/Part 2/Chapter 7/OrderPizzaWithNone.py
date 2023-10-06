def orderPizza(size, style='regular', topping=None):
    # Do some calclations based on the size and style
    # Check if a topping was specified
    PRICE_OF_TOPPING = 1.50 # Price for any topping
    
    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.0
    else:
        price = 18.0
        
    if style == 'deepdish':
        price += 2.00 # Charge extra for deepdish
        
    
    line = 'You have ordered a ' + size + ' ' + style +' pizza with '
    
    if topping is None: # check if no topping was passed in
        print(line + 'no toppings.')
    else:
        print(line  + topping)
        price = price + PRICE_OF_TOPPING
    
    
    print('The price is $', price)
    print()     
    
# You could order a pizza in the following ways:
orderPizza('large') # large, default to regular, no topping
orderPizza('large', style='regular') # same as above
orderPizza('medium', style='deepdish', topping='mushrooms')
orderPizza('small', topping='mushrooms') # style default to regular   