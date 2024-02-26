# NumPy Tutorial 7 - Handy Operations for Data Analysis

# Importing relevant modules
import numpy as np

# Operations that come in handy for data analysis!
one_dim = np.array([1, 2, 3, 4, 5])  # [1 2 3 4 5]
two_dim = np.array([[1, 2, 3], [4, 5, 6]])  # [[1 2 3] [4 5 6]]

# Summations
print(sum(one_dim))  # Produces 15
print(sum(two_dim))  # Produces [5 7 9]
print(one_dim.sum())  # Produces 15
print(two_dim.sum())  # Produces 21

# Maximum and minimum
print(two_dim.min())  # Produces 1
print(two_dim.max())  # Produces 6

# We can add elements in each row and column
two_dim2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dim2)

# Summing elements within each column
print(two_dim2.sum(axis=0))

# Summing elements within each row
print(two_dim2.sum(axis=1))
