# Employee Manager inheritance
#
# Define the Employee class, which we will use as a base class

class Employee:
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        # 52 weeks * 5 days a week * 8 hours per day
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay


class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary)  # add a bonus of 10%
            print(self.name, 'gets a bonus for good work')
        return pay


if __name__ == '__main__':
    # Create objects
    employee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
    employee2 = Employee('Chris Smith', 'Cashier', 14)
    manager = Manager('Sue Jones', 'Pizza Restaurant Manager', 55000,
                      [employee1, employee2])

    # Call methods of the Employee objects
    print('Employee name: ', employee1.getName())
    print(f'Employee salary: {employee1.payPerYear(): .2f}')
    print('Employee name: ', employee2.getName())
    print(f'Employee salary: {employee2.payPerYear(): .2f}')

    # Call methods of the Manager object
    managerName = manager.getName()
    print('Manager name: ', managerName)

    # Give the manager a bonus
    print(f'Manager salary: {manager.payPerYear(True)}, {manager.getTitle()}'
          f'direct reports: ')
    reportsList = manager.getReports()
    for employee in reportsList:
        print(' ', employee.getName(), f'({employee.getTitle()})')
