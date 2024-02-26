# NumPy Tutorial 2 - Indexing Arrays

# Importing relevant modules
import numpy as np

# Let's start indexing arrays!
# One Dimension Indexing
array = np.array([1, 2, 3, 4, 5])  # One dimensional array
print(array[0])  # This returns 1 - the first element in [1 2 3 4 5]

# Two Dimension Indexing
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
# This will return the first element of the first dimension
print(two_dim[0, 0])
# This will return the second element of the second dimension
print(two_dim[1, 1])

# Three Dimensional Indexing
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim[0, 1, 2])

# The first number (0) corresponds to the first dimension and in the first
# dimension we have, [[1 2 3] [4 5 6]] and [[7 8 9] [10 11 12]].
# Now, we have inputted 0 so this corresponds to the first element within
# this dimension. So we will return [[1 2 3] [4 5 6]].

# The second number (1) corresponds to the second dimension and in the
# second dimension, we have, [1 2 3] and [4 5 6]. Now, we have inputted
# 1 so this corresponds to the second element within this dimension.
# So, we will return [4 5 6]

# The third number (2) corresponds to the third dimension and in the third
# dimension, we have 4, 5 and 6. Now, we have inputted 2 so this corresponds
# to the third element within this dimension.

# Thus, we get 6!





