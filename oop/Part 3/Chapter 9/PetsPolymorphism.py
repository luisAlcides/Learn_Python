# Pets polymorphism
# Three classes, all with a different 'speak' method

class Dog:
    def __init__(self, name):
        self.name = name
    
    
    def speak(self):
        print(self.name, ' says bark, bark, bark! ')
    
    
class Cat:
    def __init__(self, name):
        self.name = name
        
    
    def speak(self):
        print(self.name, ' says, meeeeoowww! ')


class Bird:
    def __init__(self, name):
        self.name = name
    
    
    def speak(self):
        print(self.name, ' says tweet')
        
        
dog1 = Dog('Rover')
dog2 = Dog('Fido')
cat1 = Cat('Fluffy')
cat2 = Cat('Spike')
bird = Bird('Big Bird')

petsList = [dog1, dog2, cat1, cat2, bird]

for pet in petsList:
    pet.speak()