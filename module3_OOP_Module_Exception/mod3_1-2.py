def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the target value.

    :param sorted_list: List of sorted elements
    :param target: The value to search for
    :return: The index of the target if found, otherwise -1
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Target found at index: {index}")
else:
    print("Target not found in the list.")