from Student import *

# Main Student property example
student1 = Student('Joe Schmoe')
student2 = Student('Jane Smith')

# Get the students' grades using the 'grade' property and print
print(student1.grade)
print(student2.grade)
print()

# Set new values using the 'grade' property
student1.grade = 85
student2.grade = 92

print(student1.grade)
print(student2.grade)