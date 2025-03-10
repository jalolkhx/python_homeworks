import numpy as np
import random

matrix = np.random.randint(0, 100, (5, 5))

normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

print("Original Matrix:\n", matrix)
print("\nNormalized Matrix:\n", normalized_matrix)
