class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

m = Manager ("Ana", 80000, 5)
print("Name:", m.name)
print("Salary:", m.salary)
print("Team Size:", m.team_size)