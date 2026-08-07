'''WAP to ask the user to enter names of their 3 favorite fruits and store them in a list.'''

fruits = []
for i in range(3):
    fruit = input(f"Enter the name of your {i+1} favorite fruit: ")
    fruits.append(fruit)
print("Your favorite fruits are:", fruits)