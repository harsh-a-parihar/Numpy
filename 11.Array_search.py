import numpy as np

# search index of the number using where()--------
arr = np.array([1, 2, 3, 2, 5, 4, 2])
_index = np.where(arr == 2)     # we can find anything like, odd(arr%2==1), even(arr%2==0), etc
print('index:', _index)     # prints index at which the number is present

print('\n')     # gap

# search the indexes of numbers necessary to put in order for valid binary searching--------
arr_ = np.array([2, 3, 4, 6, 8, 9])
x = np.searchsorted(arr_, 5)    # by default index's from left
y = np.searchsorted(arr_, 5, side='right')      # index's from right
print('from left: ', x,
      'from right: ', y)

print('\n')     # gap

# try searching more than one number
any_arr = np.array([2, 3, 6, 8, 9, 11])
search_ = np.searchsorted(any_arr, [1, 4, 5, 7, 10])
print('nums should be on indexes:\n', search_)
