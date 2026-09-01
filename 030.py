'''Multiply matrices'''
import numpy as np

r1 = int(input("Rows of A: "))
c1 = int(input("Cols of A: "))
r2 = int(input("Rows of B: "))
c2 = int(input("Cols of B: "))

if c1 != r2:
    print("Multiplication not possible")
else:
    A = np.array([[int(input()) for _ in range(c1)] for _ in range(r1)])
    B = np.array([[int(input()) for _ in range(c2)] for _ in range(r2)])

    print("Product:\n", np.dot(A, B))