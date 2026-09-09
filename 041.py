'''create a class employee with name and salary as its attributes and a method to display employee details. WAP to initialise the object and display the employee details.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e = Employee("Neha", 30000)
e.display()