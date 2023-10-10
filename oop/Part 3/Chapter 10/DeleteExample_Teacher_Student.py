class Student:
    def __init__(self, name):
        self.name = name
        print('Creating Student object', self.name)

    def __del__(self):
        print('In the __del__ method for student: ', self.name)


class Teacher:
    def __init__(self):
        print('Creating the Teacher object')
        self.student1 = Student('Joe')
        self.student2 = Student('Sue')
        self.student3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')


# Instantiate the Teacher object (that creates Student objects)
teacher = Teacher()
# Delete the Teacher object
del teacher
