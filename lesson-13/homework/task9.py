import numpy as np
import random

matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))
product = np.dot(matrix1, matrix2)

print(matrix1)
print(matrix2)
print(product)