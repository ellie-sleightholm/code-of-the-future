# NumPy Tutorial 5 - Shape and Reshaping Arrays

# Importing relevant modules
import numpy as np

# Shape of an array
array = np.array([[1, 2, 3, 10], [4, 5, 6, 10], [7, 8, 9, 10]])
print(array.shape)
# This will print (3, 4) because we have 3 elements and inside
# those elements we have 4 numbers (elements)

# Notice what happens when we have different numbers of elements
# array2 = np.array([[1, 2, 3], [4, 5, 6, 7]])
# print(array2.shape)

# Reshaping arrays
# Let's suppose we have an array of student's ages and we have
# 3 students of each age
students = np.array([19, 19, 19, 20, 20, 20, 21, 21, 21])
# We also have their average exam score over the year
exam_score = np.array([57, 60, 65, 59, 63, 70, 65, 72, 75])
# Splitting up the exam score
exam_split = exam_score.reshape(3, 3)
print(exam_split)

# We can't reshape every single array! The two numbers you
# input into the reshape command must multiply together to
# create the number of elements within the original array!
exam_split2 = exam_score.reshape(9, 1)
print(exam_split2)

# Reshape into three dimensional!
one_dim = np.array([1, 2, 3, 4, 5, 6])
three_dim = one_dim.reshape(2, 3, 1)
print(three_dim)
# This will take [1 2 3 4 5 6] and break it into 2 arrays
# and inside those two arrays, it will have 3 arrays of
# 1 element.

