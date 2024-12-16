import numpy as np
from numpy.linalg import matrix_rank

# Create a random matrix
matrix = np.random.rand(4, 4)

# Compute the matrix rank
rank = matrix_rank(matrix)

print("Matrix:\n", matrix)
print("Rank of the matrix:", rank)
