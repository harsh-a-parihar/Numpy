import numpy as np      # import numpy

# create Numpy ndarray using array() function-------
array_ = np.array([10, 20, 30, 40, 50])
array_tup = np.array((10, 20, 30, 40, 50))      # create numpy array using tuple or any object type

print(array_)       # print array
print(type(array_))     # check type of array->(numpy.ndarray)
print(array_tup)
print(type(array_tup))

print('\n')     # gap

# Dimensions in arrays-------
# 0-d array
_0d_array = np.array(10)    # every single value in array is 0-d array
print(f'0-D array: {_0d_array}\n')
# 1-d array
_1d_array = np.array([10, 20, 30])      # contains 0-d values
print(f'1-D array: {_1d_array}\n')
# 2-d array
_2d_array = np.array([[10, 20, 30], [40, 50, 60]])      # contains 1-d arrays
print(f'2-D array: {_2d_array}\n')
# 3-d array
_3d_array = np.array([[[10, 20, 30], [40, 50, 60]], [[60, 50, 40], [30, 20, 10]]])      # contains 2-d arrays
print(f'3-D array: {_3d_array}')

print('\n')     # gap

# check dimension of array-------
print(_1d_array.ndim)   # 1-d
print(_2d_array.ndim)   # 2-d
print(_3d_array.ndim)   # 3-d

print('\n')     # gap

# Higher dimensional array-------
_6d_array = np.array([1, 2, 3, 4, 5], ndmin=6)     # create 6-d array
print(_6d_array)    # print value
print(_6d_array.ndim)   # print dimension
