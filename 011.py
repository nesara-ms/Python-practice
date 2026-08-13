'''WAP to check whether the given number is even or odd.''' 

def integer():
    num = int(input("Enter number:"))
    rem = num%2
    if (rem==0):
        print("EVEN")
    else:
        print("ODD")
integer()