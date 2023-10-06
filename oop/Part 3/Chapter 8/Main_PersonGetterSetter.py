from Person import *

person1 = Person("John", 10000)
person2 = Person("Jane", 20000)

# Get the salaires using getter and print
print(person1.getSalary())
print(person2.getSalary())

# Change the salaries using setter
person1.setSalary(15000)
person2.setSalary(25000)

# Get the salaries and print again
print(person1.getSalary())
print(person2.getSalary())