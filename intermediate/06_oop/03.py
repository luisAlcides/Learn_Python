# Overriding Methods

class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f'{self.name} says, Grrrr')


class Cat(Animal):
    def make_noise(self):
        print(f'{self.name} says, Meow!')


pet1 = Animal('Rex')
pet1.make_noise()
pet2 = Cat('Maisy')
pet2.make_noise()
