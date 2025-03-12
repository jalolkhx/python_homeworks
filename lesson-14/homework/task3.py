import numpy as np

matrix = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

vector = np.array([7, 4, 5])
solution = np.linalg.solve(matrix, vector)
print(solution)