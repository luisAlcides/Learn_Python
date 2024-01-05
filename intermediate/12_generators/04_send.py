""" print('Generator 1')
def count_generator():
    while True:
        n = yield 
        print(n)
        

my_generator = count_generator()
print(next(my_generator))
print(next(my_generator))
print(my_generator.send(3))

print()
print('Generator 2')
def generator():
    count = 0 
    while True:
        n = yield count
        if n is not None:
            count = n
        count += 1
        
my_generator = generator()
print(next(my_generator))
print(next(my_generator))
my_generator.send(3)
print(next(my_generator))

 """

MAX_STUDENTS = 50

def get_student_ids():
    student_id = 1
    while student_id <= MAX_STUDENTS:
        # Write your code below
        n = yield student_id
        if n is not None:
            student_id = n
            continue
        student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
    # Write your code below
    if i == 1:
        i = student_id_generator.send(25)
    print(i)
  

