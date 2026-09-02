'''Average of array'''
import numpy as np

n = int(input("Enter n: "))
arr = np.array([int(input()) for _ in range(n)])

print("Average:", np.mean(arr))