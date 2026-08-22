'''WAP to read an integer and reverse that number and print it.'''
n = int(input("Enter an integer: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reversed number:", reverse)