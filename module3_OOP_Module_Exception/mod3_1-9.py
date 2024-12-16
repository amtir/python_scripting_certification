def generate_2d_array(x, y):
    """
    Generate a 2D array where the element value in the i-th row and j-th column is i*j.
    """
    return [[i*j for j in range(y)] for i in range(x)]

# Example usage
x, y = 3, 5
array = generate_2d_array(x, y)
print(array)