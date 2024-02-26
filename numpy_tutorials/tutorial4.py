# NumPy Tutorial 4 - Copy and View

# Importing relevant modules
import numpy as np

# Copy
array = np.array([1, 2, 3, 4, 5])  # One dimensional array
copy = array.copy()  # Creates a copy of the original array
array[0] = 10  # This changes 1 to 10 (change of element)
print(array)  # This prints the array with the element change
print(copy)  # This prints the original array

# View
array2 = np.array([1, 2, 3, 4, 5])  # One dimensional array
view = array2.view()  # Creates a view of the original array
array2[0] = 10  # Changes 1 to 10 (change of element)
print(array2)  # Prints the array with the change of element
print(view)  # Prints the array with the change of element

# Python to recall whether it's a copy or a view
print(view.base)  # This will return the array (with changes)
print(copy.base)  # This will return None
