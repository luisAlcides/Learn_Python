class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    
    # Allow the caller to retrieve th salary
    def getSalary(self):
        return self.salary

    
    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salary = salary
        
    
    