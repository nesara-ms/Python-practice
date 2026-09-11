'''create a class rectangle with length and breadth as attributes and a method to find the area. invoke methods with rectangle object to read and find area.'''

class Rectangle:
    def read(self):
        self.length = float(input("Enter length: "))
        self.breadth = float(input("Enter breadth: "))

    def area(self):
        print("Area:", self.length * self.breadth)


r = Rectangle()
r.read()
r.area()