'''WAP to find perimeter of rectangle'''
def perimeter_of_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = perimeter_of_rectangle(length, width)
print("The perimeter of the rectangle is:", result)