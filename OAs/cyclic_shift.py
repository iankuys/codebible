#To check if a cyclically shifted array is reverse sorted, you can iterate through the possible shifts and check if any of them result in a reverse-sorted array. Here's a function for that:
def cyclic_shift(array, k):
    n = len(array)
    k = k % n  # Ensure k is within the range of array length

    # Perform cyclic shift using slicing
    array[:] = array[-k:] + array[:-k]

# Example usage:
my_array = [1, 2, 3, 4, 5]
cyclic_shift(my_array, 2)
print(my_array)

# check which t shifted array is reverse sorted
def cyclic_shift(array, k):
    n = len(array)
    k = k % n  # Ensure k is within the range of array length

    # Perform cyclic shift using slicing
    array[:] = array[-k:] + array[:-k]

# Example usage:
my_array = [1, 2, 3, 4, 5]
cyclic_shift(my_array, 2)
print(my_array)
