import numpy as np

# Note: splitting is opposite of joining

# split arrays using array_split() method--------------
_1darr = np.array([1, 2, 3, 4, 5, 6])
_2darr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
_new1arr = np.array_split(_1darr, 3)
_new2arr = np.array_split(_2darr, 2)
print('1-d array:\n', _new1arr)
print('2-d array:\n', _new2arr)
# we can also access splitted arrays using indexing
print('1. element:\n', _new1arr[1])
print('2. element:\n', _new2arr[1])

# Note: use hsplite() and vsplite() to split 2-d array along rows and columns
