'''Program to calculate simple interest,compound interest, and amount'''
p = int(input("Enter principal:"))
r = int(input("Enter rate:"))
t = int(input("Enter time:"))
SI = (p*r*t)/100 #Simple interest
A = p*(1+r/100)**t #Amount
CI = A - p #Compound interest
print(SI)
print(A)
print(CI)
