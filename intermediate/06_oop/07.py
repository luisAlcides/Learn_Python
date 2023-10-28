# Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f'{self.name} says Grrr')


class Cat(Animal):
    def make_noise(self):
        print(f'{self.name} says Meow!')


class Robot:
    def make_noise(self):
        print('beep.boop.....BEEEP!')


an_animal = Animal('Bear')
my_pet = Cat('Maisey')
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
    o.make_noise()


# Practice
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f'My id is: {self.id}')


class Admin(Employee):
    def say_id(self):
        super().say_id()
        print('I am an admin.')


class Manager(Admin):
    def say_id(self):
        super().say_id()
        print('I am in charge!')


meeting = [Employee(), Admin(), Manager()]

for m in meeting:
    m.say_id()