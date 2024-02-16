import numpy as np  # import numpy

# copy() function-----------
arr = np.array([1, 3, 4, 5, 6])
new_arr = arr.copy()    # copies the list
# if we change element from old_array
arr[0] = 2

print(f'old_array:{arr}')  # old_array is affected
print(f'new_array:{new_arr}')  # new_array is not affected

print('\n')     # gap

# view() function-------------
o_arr = np.array([1, 2, 3, 4, 5])
n_arr = o_arr.view()
# if we change element from o_array
o_arr[2] = 10

print(f'old_array:{o_arr}')     # old_array is affected
print(f'new_array:{n_arr}')   # new_array is also affected

print('\n')     # gap

# base() function to check diff. between copy and view-----------
a = np.array([100, 200, 300, 400, 500])
a1 = a.copy()
a2 = a.view()
print(a1.base)  # ->none
print(a2.base)  # ->value of a
