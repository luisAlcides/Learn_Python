# map
print('map')


def double(x):
    return x * 2


int_list = [3, 6, 9]
doubled = map(double, int_list)

print('With functions: ', list(doubled))

doubled = map(lambda input: input * 2, int_list)
print('Without functions: ', list(doubled))

# Practice
grade_list = [3.5, 3.7, 2.6, 95, 87]
grades_100scale = map(lambda grade: grade * 25 if type(grade) is float else grade, grade_list)
print(list(grades_100scale))

# filter
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]

M_names = filter(lambda name: name[0] == 'M' or name[0] == 'm', names)
print()
print('filter')
print(list(M_names))

books = [["Burgess", 1985],
         ["Orwell", "Nineteen Eighty-four"],
         ["Murakami", "1Q85"],
         ["Orwell", 1984],
         ["Burgess", "Nineteen Eighty-five"],
         ["Murakami", 1985]]


string_titles = filter(lambda book: isinstance(book[1], str), books)
print(list(string_titles))

# Reduce
from functools import reduce
print()
print('Reduce')
print(int_list)
int_list = [3, 6, 9, 12]

reduced_int_list = reduce(lambda x, y: x*y, int_list)
print(reduced_int_list)

# Practice
letters = ['r', 'e', 'd', 'u', 'c', 'e']
word = reduce(lambda w, o: str(w+o), letters)
print(word)

