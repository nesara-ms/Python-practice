'''To generate a random 6 digit password comprising lowercase letters, uppercase letters, digits and special characters.'''
import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = ""

for i in range(6):
    password += random.choice(characters)

print(password)