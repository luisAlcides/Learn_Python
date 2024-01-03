import itertools


""" even = [2, 4, 6]
even_combinations = list(itertools.combinations(even, 2))
print(even_combinations)
 """
 
collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]
collar_combo_iterator = itertools.combinations(collars, 3)

for collar in collar_combo_iterator:
    print(collar)