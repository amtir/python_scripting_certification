# Find numbers divisible by 7 but not a multiple of 5, between 2000 and 3200
numbers = [str(number) for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0]

# Print the numbers in a comma-separated sequence
print(",".join(numbers))