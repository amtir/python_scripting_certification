import math

# Example list of floating point numbers
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Using sum
sum_result = sum(numbers)
print(f"Result using sum: {sum_result}")

# Using math.fsum for better precision with floating point numbers
fsum_result = math.fsum(numbers)
print(f"Result using math.fsum: {fsum_result}")