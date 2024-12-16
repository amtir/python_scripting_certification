def remove_duplicates_sort(input_string):
    """
    Remove duplicate words and sort the remaining words alphanumerically.
    """
    words = input_string.split()
    unique_words = sorted(set(words))
    return ' '.join(unique_words)

# Example usage
input_string = "hello world and practice makes perfect and hello world again"
result = remove_duplicates_sort(input_string)
print(result)