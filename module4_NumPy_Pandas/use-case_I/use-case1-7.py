import numpy as np

# Create the numpy array with NaN values
arr = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])

# Print the original array
print("Original array:", arr)

# Omit NaN elements and print
filtered_arr = arr[~np.isnan(arr)]
print("Array without NaN:", filtered_arr)