# NumPy Tutorial 10 - Searching in Arrays

# Importing relevant modules
import numpy as np

# We can search in a given array to tell whether an element
# is located in there!

# One dimensional array
array1 = np.array([1, 2, 3, 4, 4, 6, 8, 9, 9, 8])
# Finding if a given value is in this array!
location = np.where(array1 == 4)
print(location)
# This prints '(array([3, 4]),)' and this tells us that
# the number 4 is located at index 3 and index 4!

# You can do more than just locate whether an element is in
# an array
less_than_five = np.where(array1 < 5)
print(less_than_five)

# Let's see if elements in this array are divisible by 3
divisible_by_three = np.where(array1%3 == 0)
print(divisible_by_three)