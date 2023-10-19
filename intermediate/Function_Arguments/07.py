def single_prix_fixe_order(appetizer, *entrees, sides, **desert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(desert_scoops)


single_prix_fixe_order('Baby Beets',
                       'Salmon', 'Scallops',
                       sides='Mashed Potatoes',
                       scoop='Vanilla', dessert='Cookies and Cream')