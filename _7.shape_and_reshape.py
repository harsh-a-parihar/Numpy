import numpy as np

# shape() function---------
_6d_arr = np.array([10, 20, 30], ndmin=6)
print(_6d_arr)  # print array
print('shape:', _6d_arr.shape)  # print shape of array

print('\n')     # gap

# reshape() function---------
shaped_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print('shaped_array:\n', shaped_arr)
print('reshaped_array:\n', shaped_arr.reshape(4, 3))  # reshape old_array and convert 1-d to 2-d
print('reshaped_array:\n', shaped_arr.reshape(2, 3, -1))  # reshape old_array and convert 1-d to 3-d, -1 detects dim
# check if the reshape returns copy or view using base
print(shaped_arr.reshape(4, 3).base)    # original array -> view

print('\n')     # gap

# convert multidimensional arrays into 1-d----------------
mul_arr = np.array([[[10, 20, 30], [30, 20, 10]]])
print('2-d array:\n', mul_arr)
con_arr = mul_arr.reshape(-1)   # automatically converts to 1-d array
print('1-d array:\n', con_arr)
