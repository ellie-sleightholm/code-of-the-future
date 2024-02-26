# NumPy Tutorial 11 - Sorting in Arrays

# Importing relevant modules
import numpy as np

# Sorting Arrays
# In NumPy, we have a function called 'sort'.

# This will sort an array in mathematical order
array1 = np.array([1, 983, -28, 8, 10, -73, -18743, 2987532])
array1_sorted = np.sort(array1)
print(array1_sorted)

# We can sort two-dimensional arrays!
array2 = np.array([[91, -45, 9], [8, -3, 4]])
array2_sorted = np.sort(array2)
print(array2_sorted)

# We don't just have to have numbers in an array!
boolean_array = np.array([True, False, True, False, False])
ba_sorted = np.sort(boolean_array)
print(ba_sorted)

# Let's sort an array with strings into alphabetical order
string_array = np.array(['London', 'Somerset', 'York', 'Aberdeen'])
sa_sorted = np.sort(string_array)
print(sa_sorted)

# Another cool function in NumPy - 'searchsorted'.
# This command will return the index where the inputted value
# would need to be placed in order to maintain order.
array3 = np.array([1, 3, 5, 6])
location = np.searchsorted(array3, 4)
print(location)

location2 = np.searchsorted(array3, [2, 4, 9])
print(location2)


