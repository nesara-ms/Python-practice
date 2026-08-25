'''WAP to print alphabet from A to Z using for loop'''
def print_alphabet():
    for i in range(65, 91):  # ASCII values for A-Z
        print(chr(i), end=' ')

print_alphabet()