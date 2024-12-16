import numpy as np

# Create a 10x10 array with random values
arr = np.random.random((10, 10))

# Find the minimum and maximum values
min_val = arr.min()
max_val = arr.max()

print(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)