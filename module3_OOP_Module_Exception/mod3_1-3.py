import time

def is_it_dark():
    """
    Determine if it's dark based on the current local time.
    Considering dark hours from 7pm to 6am.
    """
    current_time = time.localtime()  # Get struct_time for local time
    hour = current_time.tm_hour  # Extract the hour from struct_time

    # Check if it's dark
    if hour >= 19 or hour < 6:
        return True
    else:
        return False

# Example usage
if is_it_dark():
    print("It's dark outside.")
else:
    print("It's not dark outside.")