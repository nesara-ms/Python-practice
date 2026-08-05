'''Program: Admission Fee Calculator

This program calculates the admission fee based on a person's age
and gender using conditional statements (if-elif-else).'''

# Get user input
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()

# Calculate fee (by using conditional statements and logical operators)
if (age == 1 or age == 2) and gender == "M":
    print("Fee is 100")
elif age == 3 or age == 4 or gender == "F":
    print("Fee is 200")
elif age == 5 and gender == "M":
    print("Fee is 300")
else:
    print("No fee")