'''WAP using numpy to add two matrices. Read order matrices and elements'''

import numpy as np

r = int(input("Rows: "))
c = int(input("Columns: "))

print("Enter first matrix:")
A = np.array([[int(input()) for _ in range(c)] for _ in range(r)])

print("Enter second matrix:")
B = np.array([[int(input()) for _ in range(c)] for _ in range(r)])

print("Sum:\n", A + B)
