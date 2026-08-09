'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. (use subject name as key and marks as value)'''
#lets us say the subjects are Maths, Science and Kannada
marks = {}

x = int(input("Enter maths:"))
marks.update({'Maths': x}) 

y = int(input("Enter science:"))
marks.update({'Science': y}) 

z = int(input("Enter kannada:"))
marks.update({'Kannada': z}) 

print(marks)