def filter_divisible_by_5(binary_numbers):
    """
    Check which binary numbers are divisible by 5 and print them in a comma-separated sequence.
    """
    divisible_by_5 = [num for num in binary_numbers.split(',') if int(num, 2) % 5 == 0]
    return ','.join(divisible_by_5)

# Example usage
binary_numbers = "0100,0011,1010,1001"
result = filter_divisible_by_5(binary_numbers)
print(result)