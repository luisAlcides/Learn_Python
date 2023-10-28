# Dunder Methods
# For a list and a list, + returns a list
if [1, 2] + [3, 4] == [1, 2, 3, 4]:
    print(True)


class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __add__(self, another_animal):
        return Animal(self.name + another_animal.name)


a1 = Animal('Horse')
a2 = Animal('Penguin')
a3 = a1 + a2
print(a1)
print(a2)
print(a3)


# Practice
class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        print(f'ID {employee.id} added.')
        self.attendees.append(employee)

    def __len__(self):
        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Employee()

m1 = Meeting()

m1 + e1
m1 + e2
m1 + e3

print(len(m1))

# employees = [e1, e2, e3]
#for e in employees:
    #m1.__add__(e)
#print(m1.__len__())


