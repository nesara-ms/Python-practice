'''create a class student with name and usn as attributes and a method to display the details. invoke the display method with a student objects. '''
class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn

    def display(self):
        print("Name:", self.name)
        print("USN:", self.usn)


s = Student("Alex", "1AB23CS001")
s.display()