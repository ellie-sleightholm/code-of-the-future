# NumPy Tutorial 3 - Slicing Arrays

# Importing relevant modules
import numpy as np

# Slicing One Dimensional Arrays
one_dim = np.array([1, 2, 3, 4, 5])  # One Dimensional Array
# This will return elements from the first element to the 4th element, [1 2 3 4]
print(one_dim[0:4])
# This will return elements from the second element to the third element, [2 3]
print(one_dim[1:3])
# This will return the entire array (unless we input some extra values)
print(one_dim[:])
# We can recall elements in steps
print(one_dim[:5:2])

# Considering Two Dimensional Array Slicing
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
# This will return a slice from the first element to the second element from the
# second dimension, [4 5]
print(two_dim[1, 0:2])

# Creating another two dimensional array
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# From all elements, slice from index 0 to index 2
print(two_dim2[0:3, 0:2])


