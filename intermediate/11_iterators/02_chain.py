import itertools

""" odd = [5, 7, 9]
even = {6, 8, 10}

all_numbers = itertools.chain(odd, even)

for number in all_numbers:
    print(number) """
    
    
great_dane_foods = [2439176, 3174521, 3560031]
min_pin_pup_foods = [6821904, 3302083]
pawsome_pup_foods = [9664865]


all_skus_iterator = itertools.chain(great_dane_foods, min_pin_pup_foods, pawsome_pup_foods)

for sku in all_skus_iterator:
    print(sku)