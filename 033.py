'''Average of elements greater than value'''
import numpy as np
n = int(input("Enter n: "))
arr = np.array([int(input()) for _ in range(n)])

val = int(input("Enter value: "))
filtered = arr[arr > val]

print("Average:", np.mean(filtered) if len(filtered) > 0 else 0)