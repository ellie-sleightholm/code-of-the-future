# NumPy Tutorial 8 - Iterating Arrays

# Importing relevant modules
import numpy as np

# Creating a one dimensional array
one_dim = np.array([1, 2, 3, 4, 5])  # [1 2 3 4 5]

# Iterate over a one dimensional array!
for element in one_dim:
    print(element)

# Creating a two dimensional array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])  # [[1 2 3] [4 5 6]]

# Iterate over a two dimensional array!
for element in two_dim:
    for number in element:
        print(number)

# Using 'nditer' ! Really handy way of iterating without lots
# of for loops!!
for element in np.nditer(two_dim):
    print(element)

# Figuring out the index - using 'ndenumerate'
for index, element in np.ndenumerate(two_dim):
    print(index, element)

