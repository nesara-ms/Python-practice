'''WAP to return multiple values by reading two integers after performing addition and multiplication.'''
def calculate(a, b):
    addition = a + b
    multiplication = a * b
    return addition, multiplication
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
add, mult = calculate(a, b)
print("Addition:", add)
print("Multiplication:", mult)