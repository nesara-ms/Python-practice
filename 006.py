'''print right triangle number pattern using for loop'''

row = int(input("Enter number of rows:")) 

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()