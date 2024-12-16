def count_case(sentence):
    """
    Calculate the number of upper case and lower case letters in a sentence.
    """
    upper_case = sum(1 for char in sentence if char.isupper())
    lower_case = sum(1 for char in sentence if char.islower())
    return f"UPPER CASE {upper_case}\nLOWER CASE {lower_case}"

# Example usage
sentence = "Hello world!"
result = count_case(sentence)
print(result)