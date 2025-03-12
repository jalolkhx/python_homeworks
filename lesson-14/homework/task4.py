import numpy as np

matrix = np.array([
    [10, 2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

vector = np.array([12, -5, 15])
solution = np.linalg.solve(matrix, vector)
print(solution)