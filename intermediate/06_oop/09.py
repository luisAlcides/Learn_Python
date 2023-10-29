# Abstraction
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_noise(self):
        pass


class Cat(Animal):
    def make_noise(self):
        print(f'{self.name} says, Meow!')


class Dog(Animal):
    def make_noise(self):
        print(f'{self.name} says, Woof')


kitty = Cat('Missy')
doggy = Dog('Amber')
kitty.make_noise()
doggy.make_noise()


# Practice --------------------------------------------
class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class Employee(AbstractEmployee):
    def say_id(self):
        print(self.id)


e1 = Employee()
e1.say_id()