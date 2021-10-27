#products: to find the product of the elements in an array, use the prod() function
#-> tìm tích

import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr) #-> 1*2*3*4 = 24
print(x)
print("--------------------------")
#find the product of the elements of two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])#
print(x) # -> 1*2*3*4*5*6*7*8
print("--------------------------")

#product over an axis
# if axis = 1, numpy will return the product of each array
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
print("--------------------------")

#cummulative product: [1, 2, 3, 4] -> [1, 1*2, 1*2*3, 1*2*3*4]
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)
