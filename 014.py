'''WAP to check frequency count of each character in a string.'''
def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
string = input("Enter a string: ")
frequency_count = char_frequency(string)
print("Character frequency count:")
for char, count in frequency_count.items():
    print(f"'{char}': {count}")
