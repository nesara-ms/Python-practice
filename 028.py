'''To reverse a string, without slicing.'''
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
s = input("Enter a string: ")
reversed_s = reverse_string(s)
print("Reversed string:", reversed_s)