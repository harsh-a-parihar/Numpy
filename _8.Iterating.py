import numpy as np

# iterate array using nditer() function------------
_3darr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(_3darr):
    print(i)    # prints scaler elements

print('\n')     # gap

# iterate array with diff. data types----------
arr = np.array([10, 20, 30])
for i in np.nditer(arr, flags=['buffered'], op_dtypes='S'):
    print(i)    # prints array values in string form

print('\n')     # gap

# iterate with index and value using ndenumerate()-----------
arr1 = np.array([10, 20, 30])
for ind, val in np.ndenumerate(arr1):
    print(ind, val)     # prints index and value at that index

