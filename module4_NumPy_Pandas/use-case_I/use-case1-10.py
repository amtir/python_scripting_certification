import numpy as np

# Create numpy array with elements 0 to 10
arr = np.arange(11)
print(arr)
# Negate all elements between 3 and 9
arr[(arr > 3) & (arr < 9)] *= -1

print(arr)