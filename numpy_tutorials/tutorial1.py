# NumPy Tutorial 1 - Creating Arrays and Dimensional Arrays

# Importing relevant modules
import numpy as np

# Creating a simple array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Let's explore the different size dimensions

# Zero Dimensional Array
zero_dim = np.array(382759138)
print(zero_dim)

# One Dimensional Array
one_dim = np.array([1, 2, 3])
print(one_dim)

# Two Dimensional Array
two_dim = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim)

# Three Dimensional Array
three_dim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_dim)

# Finding the dimension of a given array
print(two_dim.ndim)  # this prints the dimension of a given array

# Give an array any dimension you want!
new_array = np.array(17, ndmin=5)
print(new_array)
