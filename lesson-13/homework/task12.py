import numpy as np
import random

A = np.random.randint(1, 10, (3, 4))
B = np.random.randint(1, 10, (4, 3))

print(A)
print(B)

C = np.dot(A, B)
print(C)