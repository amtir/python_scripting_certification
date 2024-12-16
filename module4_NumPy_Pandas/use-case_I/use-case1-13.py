import numpy as np

# Create a random array of shape (5, 5) for demonstration
arr = np.random.rand(5, 5)
print(arr)
# Swap row 1 with row 3 (0-indexed)
arr[[1, 3]] = arr[[3, 1]]

print("Array after swapping rows:\n", arr)