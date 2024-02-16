import numpy as np

# add two 1-d arrays using concatenate()----------
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
add1d = np.concatenate((arr1, arr2))
print('added array:\n', add1d)

print('\n')     # gap

# add two 2-d arrays using concatenate()----------
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
add2d = np.concatenate((a1, a2), axis=1)
print('added array:\n', add2d)

print('\n')     # gap

# join array using stack() method------------
array_1 = np.array([0, 1, 2])
array_2 = np.array([3, 4, 5])
ad = np.stack((array_1, array_2), axis=1)
print('added array:\n', ad)

print('\n')     # gap

# hstack() to stack along rows-------------
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
addition = np.hstack((arr_1, arr_2))
print('added array(along row):\n', addition)

print('\n')     # gap

# vstack() to stack along columns--------------
_1arr = np.array([1, 2, 3])
_2arr = np.array([4, 5, 6])
_add = np.vstack((_1arr, _2arr))
print('added array(along column):\n', _add)

print('\n')     # gap

# dstack() to stack along height----------------
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
adding_ = np.dstack((array1, array2))
print('added array(along height/depth):\n', adding_)
