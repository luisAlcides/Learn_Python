# super


class Animal:
    def __init__(self, name, sound='Grrr'):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print(f'{self.name} says, {self.sound}')


class Cat(Animal):
    def __init__(self, name, sound='Meow'):
        super().__init__(name, sound)


pet_cat = Cat('Rachel')
pet_cat.make_noise()