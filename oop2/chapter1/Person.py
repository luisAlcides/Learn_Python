class Person:
    # Class object attribute
    is_person = True

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = name
        self.age = age

    def greet(self):
        print(f'{self.name}')
        print(f'{self.lastname}, old: {self.age}')
        print(f'Called by the class itself: {Person.is_person}.')
        print(f'Called by the self keyword: {self.is_person}')

    # class method
    @classmethod
    def date_created(cls, today_date, year):
        print(today_date, year)

    @staticmethod
    def is_adult(age):
        return age >= 18


person_obj1 = Person('Norma', 'Rodrigues', 17)
person_obj1.date_created('14/05', 2023)
print(person_obj1.greet())
print(person_obj1.is_adult(17))
