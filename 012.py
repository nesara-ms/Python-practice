'''WAP to check whether the given year is leap year or not.'''
def leap_year():
    year = int(input("Enter year:"))
    if (year%4==0 and year%100!=0) or (year%400==0):
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")
leap_year()
