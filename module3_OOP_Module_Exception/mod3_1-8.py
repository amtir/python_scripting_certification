import math

def calculate_q(d_values):
    """
    Calculate and print the value of Q for each given D, using the formula:
    Q = Square root of [(2 * C * D)/H]
    """
    C = 50
    H = 30
    results = []
    for D in d_values:
        Q = math.sqrt((2 * C * D) / H)
        results.append(int(Q))
    return results

# Example usage
d_values = [100, 150, 180]
results = calculate_q(d_values)
print(",".join(map(str, results)))