'''Program to create and display file'''
f = open("sample.txt", "w")
f.write("Hello\nWelcome to Python\nFile Handling")
f.close()

f = open("sample.txt", "r")
for line in f:
    print(line.strip())
f.close()