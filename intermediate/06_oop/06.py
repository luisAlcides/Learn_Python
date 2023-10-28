# Multiple Inheritance: Part 2

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def action(self):
        print(f'{self.name} wags tail. Awwwww')


class Wolf(Animal):
    def action(self):
        print(f'{self.name} bites. OUCH!')


class Hybrid(Dog, Wolf):
    def action(self):
        super().action()
        Wolf.action(self)


my_pet = Hybrid('Fluffy')
my_pet.action()


# Practice
class Employee():
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My id is: {self.id}')


class User:
    def __init__(self, username, role='Customer'):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f'My username is: {self.username}')
        print(f'My role is: {self.role}')


class Admin(Employee, User):
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, 'Admin')

    def say_id(self):
        super().say_id()
        print('I am an admin')


e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()
