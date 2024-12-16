import numpy as np

# Create the numpy array
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

# Filter elements greater than 5
filtered_arr = arr[arr > 5]

print(filtered_arr)