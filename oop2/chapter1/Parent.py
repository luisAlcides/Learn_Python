# Parent
class Person(object):
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

    def info(self):
        print(f'Name: {self.name}')
        print(f'dob: {self.dob}')
        print(f'id: {self.id_number}')


# Child class
class Employee(Person):
    def __init__(self, name, dob, id_number, salary, position):
        # invoking the __init__ of the parent class
        Person.__init__(self, name, dob, id_number)
        self.salary = salary
        self.position = position

    def info(self):
        print(f'name: {self.name}')
        print(f'dob: {self.dob}')
        print(f'id: {self.id_number}')
        print(f'salary: {self.salary}')
        print(f'Position: {self.position}')


# Instance of Person class
print('# Instance of Person class')
person_obj = Person('Andy', '29/09/1999', 1334524)
person_obj.info()
print()

print('# Instance of Employee class')
employee_obj = Employee('James', '29/09/1999', 1334524, 7000, 'accountant')
employee_obj.info()
