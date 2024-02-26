# NumPy Tutorial 9 - Joining Arrays

# Importing relevant modules
import numpy as np

# Joining Arrays

# Create two one dimensional arrays
array1 = np.array([1, 2, 3, 4, 5])  # [1 2 3 4 5]
array2 = np.array([6, 7, 8, 9, 10])  # [6 7 8 9 10]
# Concatenating/join these two arrays together
joined_array = np.concatenate((array1, array2))
print(joined_array)

# Join arrays along rows
array3 = np.array([[1, 2, 3], [4, 5, 6]])  # [[1 2 3] [4 5 6]]
array4 = np.array([[7, 8, 9], [10, 11, 12]])  # [[7 8 9] [10 11 12]]
print(array3)
print(array4)
joined_row_array = np.concatenate((array3, array4), axis=1)
print(joined_row_array)

# Split Arrays
# One dimensional array:
arr = np.array([1, 2, 3, 4, 5, 6])  # [1 2 3 4 5 6]
split_array = np.array_split(arr, 3)
print(split_array)
# Recalling elements within 'split_array' - returns the split
# arrays in a nice format!
print(split_array[0])
print(split_array[1])
print(split_array[2])

