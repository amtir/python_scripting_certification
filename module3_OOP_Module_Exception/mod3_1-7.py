def factorial(n):
    """
    Compute the factorial of a given number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage
n = 8
print(f"The factorial of {n} is: {factorial(n)}")