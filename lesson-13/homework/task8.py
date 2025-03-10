import numpy as np
import random

matrix5x3 = np.random.randint(1, 100, (5, 3))
matrix3x2 = np.random.randint(1, 100, (3, 2))
print(matrix5x3)
print(matrix3x2)

product = np.dot(matrix5x3, matrix3x2)
print(product)