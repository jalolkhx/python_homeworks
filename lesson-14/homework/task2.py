import numpy as np

arr1 = np.array([2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4])

@np.vectorize
def power(a, b):
    return pow(a, b)

print(power(arr1, arr2))