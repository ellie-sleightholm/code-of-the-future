# NumPy Tutorial 6 - Basic Operations on Arrays

# Importing relevant modules
import numpy as np

# We can create an array between numbers like we can do with
# lists and the 'range' command.
# When using arrays, we use the 'arange' command.
# This will produce [0 1 2 3 4] (remember it's 4 not 5!!)
a = np.arange(0, 5)
print(a)

# Basic mathematical operations on arrays
b = np.array([4, 6, 19, 23, 45])  # [4 6 19 23 45]

# Adding
print(a + b)  # Produces [4 7 21 26 49]
# Subtracting
print(b - a)  # Produces [4 5 17 20 41]
# Square all the elements in the array 'a'.
print(a**2)  # Produces [0 1 4 9 16]

# NumPy actually has it's own functions built
print(np.sqrt(a**2))  # Produces [0. 1. 2. 3. 4.]

# Multiplying everything in 'a' by 3
print(a*3)  # Produces [0 3 6 9 12]

# Testing whether values in an array are less than a given value
c = np.array([1, 2, 3, 4])
print(c < 2)  # This prints an array of Booleans
# [True False False False]



