# Multiple inheritance: part 1

class Animal:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f'{self.name} says, Hi!')


class Cat(Animal):
    pass


class Angry_Cat(Cat):
    pass


my_pet = Angry_Cat('Mr. Cranky')
my_pet.say_hi()
