def sort_words(input_string):
    """
    Sort a comma-separated sequence of words alphabetically.
    """
    words = input_string.split(',')
    words.sort()
    return ','.join(words)

# Example usage
input_string = "without,hello,bag,world"
sorted_string = sort_words(input_string)
print(sorted_string)