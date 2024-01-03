from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_iterator = iter(student_roster)


for _ in range(len(student_roster)):
    student_info = next(student_iterator)
    print(student_info)
    

organizer = ClassroomOrganizer()
print()
print('Students sorted')
for student_name in organizer:
    print(student_name)
    
print()
print('Combinations')
table_combinations = organizer.get_table_combinations()
print(table_combinations)
print()
print('Math and science')
math_science_combinations = organizer.get_math_and_science_combinations()
print(math_science_combinations)