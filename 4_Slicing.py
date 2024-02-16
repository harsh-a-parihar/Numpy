import numpy as np      # import numpy

# Slicing array----------
_arr1 = np.array([1, 2, 3, 4, 5])
_arr2 = np.array([[10, 20, 30], [40, 50, 60]])

print(_arr1[1:4])   # [2, 3, 4]
print(_arr1[0:])   # [1, 2, 3, 4, 5]
print(_arr1[0:5:2])    # [1, 3, 5]
print(_arr2[1:, 0:3])    # [[40, 50]]
