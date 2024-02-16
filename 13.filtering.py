import numpy as np

# filtering in the array------------
arr = np.array([22, 23, 24, 25])
bool_ = [True, True, False, False]
new_arr = arr[bool_]     # here the new_arr contains those values for which the elements in the arr is True
print(new_arr)

print('\n')     # gap

# filtering in the arrays using condition----------
arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr1:
    # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr1 = arr1[filter_arr]
print(filter_arr)
print(newarr1)
