'''create a class called Account having name,id and balance as attributes.Define methods to initialize the objects, display attributes, deposit amount and withdraw amount. invoke methods to show various operations.'''
class Account:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


a = Account("Neha", 101, 5000)

a.display()
a.deposit(2000)
a.withdraw(1000)

print("\nFinal Details:")
a.display()