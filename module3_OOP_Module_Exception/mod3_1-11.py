def capitalize_lines():
    """
    Accepts sequence of lines as input and prints the lines after capitalizing all characters.
    """
    lines = []
    while True:
        line = input("Enter line (or leave blank to finish): ")
        if not line:
            break
        lines.append(line.upper())

    for line in lines:
        print(line)

# Example usage
capitalize_lines()