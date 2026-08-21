'''To print elements of list in a single line'''
cities = ["bengaluru" , "mumbai", "delhi", "chennai", "kolkata"]
foods = ["idli", "vada", "dosa", "samosa", "pani puri"]
def print_length(lst):
    for i in lst:
        print(i, end=" ")
    print()  # for new line after printing all elements

print_length(cities)
print_length(foods)