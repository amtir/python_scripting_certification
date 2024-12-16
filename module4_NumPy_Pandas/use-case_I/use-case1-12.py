import numpy as np

# Create a four dimensions array
arr = np.random.rand(4, 4, 4, 4)
#print(arr)
# Get sum over the last two axis at once
sum_over_last_two = arr.sum(axis=(-2, -1))

print(sum_over_last_two)