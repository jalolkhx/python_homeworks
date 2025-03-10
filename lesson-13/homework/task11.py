import numpy as np
import random

matrix1 = np.random.randint(1, 10, (3, 3))
det_matrix1 = np.linalg.det(matrix1)
print(matrix1)
print(f"{det_matrix1:.2f}")