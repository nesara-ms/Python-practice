'''create a class called circle with radius as attribute and a method to read radius and find the area. Invoke the method to display area of circle.'''
import math

class Circle:
    def read(self):
        self.radius = float(input("Enter radius: "))

    def area(self):
        print("Area of circle:", math.pi * self.radius ** 2)

c = Circle()
c.read()
c.area()