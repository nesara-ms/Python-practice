'''using math module to find GCD of two numbers'''

import math

def gcd(a, b):
    return math.gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD:", gcd(a, b))