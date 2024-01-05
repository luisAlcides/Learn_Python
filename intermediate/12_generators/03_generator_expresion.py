
a_list = [i * i for i in range(4)]
a_generator = (i * i for i in range(4))
print('List comprehensions: ', a_list)
print('Generator comprehensions: ', next(a_generator))


def cs_generator():
    for i in range(1, 5):
        yield 'Computer Science ' + str(i)

cs_courses = cs_generator()

for courses in cs_courses:
    print(courses)
    

# Generator comprehensions
cs_generator_exp = ('Computer Science ' + str(i) for i in range(1, 5))