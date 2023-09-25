class Persona:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        
        
    def __str__(self):
        return "Nombre: " + self.name + " Apellido: " + self.lastname + " Edad: " + str(self.age)

persona1 = Persona("Juan", "Perez", 28)
print(persona1)