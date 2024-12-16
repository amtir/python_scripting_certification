import numpy as np

# Create a random array of 3 rows and 3 columns
arr = np.random.random((3, 3))

# Sort according to the 1st column
arr_sorted_1st_col = arr[arr[:, 0].argsort()]

# Sort according to the 2nd column
arr_sorted_2nd_col = arr[arr[:, 1].argsort()]

# Sort according to the 3rd column
arr_sorted_3rd_col = arr[arr[:, 2].argsort()]

print("Original array:\n", arr)
print("Sorted by 1st column:\n", arr_sorted_1st_col)
print("Sorted by 2nd column:\n", arr_sorted_2nd_col)
print("Sorted by 3rd column:\n", arr_sorted_3rd_col)