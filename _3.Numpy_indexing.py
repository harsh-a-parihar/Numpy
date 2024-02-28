import numpy as np      # import numpy

# indexing using numpy--------------
_array1 = np.array([11, 22, 33, 44, 55])     # create 1-d array
_array2 = np.array([[1, 2, 3], [4, 5, 6]])      # create 2-d array
_array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])   # 3-d create array

print(_array1[2])   # number at index->33
print(_array1[0])    # number at index->11
print(_array2[0:1])     # number at index->from 0 to 1(excluded)
print(_array3[0:1:2])   # number at index->from 0 to 1 but steps=2
