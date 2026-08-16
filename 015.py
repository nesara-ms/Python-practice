'''WAP to check whether the given number is prime or not.'''
num = int(input("Enter number:"))
flag = 0
for i in range(2,num//2+1):
    if (num%i==0):
        print(num,"is not a prime number")
        flag = 1
        break
if (flag==0):
    print(num,"is a prime number")