'''FIND VOWELS IN A STRING'''

str = "hello,good morning"

vowels = "aeiou"

for char in str:
    for vowel in vowels:
        if char == vowel:
            print(char)