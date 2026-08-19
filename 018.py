'''WAP to swap two floating point numbers without using third variable'''
a = float(input("Enter the first floating point number: "))
b = float(input("Enter the second floating point number: "))
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)
