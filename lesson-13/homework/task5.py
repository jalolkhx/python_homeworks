import numpy as np
import random

arr1 = np.random.randint(1, 100, (3, 3, 3))
print("the array:")
print(arr1)
maxValue = np.max(arr1)
minValue = np.min(arr1)
print(f"The max value is {maxValue}")
print(f"The min value is {minValue}")