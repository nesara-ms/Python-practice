'''program to calculate average of three numbers'''
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

print("Enter three numbers:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = calculate_average(num1, num2, num3)
print(f"The average is: {result}")