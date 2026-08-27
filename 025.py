'''WAP to remove duplicates from a string'''
def remove_duplicates(string):
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result
string = input("Enter a string: ")
string_without_duplicates = remove_duplicates(string)
print("String without duplicates:", string_without_duplicates)