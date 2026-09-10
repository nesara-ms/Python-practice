'''menu driven program'''

class Account:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def display(self):
        print("\nName:", self.name)
        print("ID:", self.id)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")


name = input("Enter name: ")
id = input("Enter ID: ")
balance = float(input("Enter initial balance: "))

a = Account(name, id, balance)

while True:
    print("\n1. Display")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a.display()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        a.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        a.withdraw(amount)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")