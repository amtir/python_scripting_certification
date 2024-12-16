import numpy as np

# Given array of integers
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

# Use np.bincount to count occurrences of each value
counts = np.bincount(arr)

print(counts)


