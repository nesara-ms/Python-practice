'''WAP to replace vowels in a string with *'''
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        string = string.replace(char, "*")
print("String after replacing vowels with *:", string)