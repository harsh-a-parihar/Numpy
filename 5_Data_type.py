import numpy as np      # import numpy

# find data_type of array------------
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1.dtype)   # check type of array

arr2 = np.array(['harsh', 'abhijeet', 'r_kumar'])
print(arr2)
print(arr2.dtype)   # check type of array

print('\n')     # gap

# create array with any data_type-----------
arri_ = np.array([3, 4, 5, 6, 7], dtype='i')
print(arri_)
print(arri_.dtype)      # check type of array
arr_ = np.array([1, 2, 3, 4], dtype='S')
print(arr_)
print(arr_.dtype)       # check type of array

# Note: String value/element cannot be converted into integer

print('\n')     # gap

# change data type of existing array-----------
old_array = np.array([1.1, 1.2, 1.3, 1.4, 1.5])     # array of float values
print(old_array, old_array.dtype)
new_array = old_array.astype(int)       # copies old array and converts values into 'int'/'str'/'bool'/'float'
print(new_array, new_array.dtype)       # print new array
