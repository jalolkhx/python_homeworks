import numpy as np

# Create a 5x5 matrix with random integers (1 to 10)
A = np.random.randint(1, 10, (5, 5))

# Compute row-wise sum (sum along axis=1)
row_sums = np.sum(A, axis=1)

# Compute column-wise sum (sum along axis=0)
col_sums = np.sum(A, axis=0)

# Print results
print("Matrix A:\n", A)
print("\nRow-wise sums:\n", row_sums)
print("\nColumn-wise sums:\n", col_sums)
