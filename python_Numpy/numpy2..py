        #datatype in numpy
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - String
U - unicode string
V - void
"""
import numpy as np
i_arr = np.array([1,2,3,4])
print(i_arr.dtype)
s_arr = np.array(["apple", "banana", "cherry"])
print(s_arr.dtype)
print("------------------------")
#create array with defined dtype
s_arr_create = np.array([1,2,3,4,5], dtype="S")
print(s_arr_create)
print(s_arr_create.dtype)
print("------------------------")
#i_arr_create = np.array(['a', '2', '3'], dtype='i') -> cannot convert -> error
#print(i_arr_create)
#converting data type
f_arr_create = np.array([1.1, 2.1, 3.1])
newarr_i = f_arr_create.astype('i')
print(newarr_i)
print(newarr_i.dtype)
i_arr_create = np.array([1, 0, 3])
newarr_b = i_arr_create.astype(bool)
print(newarr_b)
print(newarr_b.dtype)
print("------------------------")
            #copy and view
#copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
print(x.base)
print("------------------------")
#view
arr1 = np.array([1, 2, 3, 4, 5])
y = arr1.view()
y[0] = 31
print(arr1)
print(y)
print(y.base)
print("------------------------")
            #shape of the array
arr_shape = np.array([[1,2,3,4],[5,6,7,8]])
print(arr_shape.shape)
arr_shape2 = np.array([1,2,3,4], ndmin = 5)
print(arr_shape2)
print("shape of array:", arr_shape2.shape)
print("------------------------")
            #array reshape
#reshape from 1D -> 2D
arr_reshape = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr_reshape_2 = arr_reshape.reshape(4,3)
print(newarr_reshape_2)
#reshape from 1D -> 2D
newarr_reshape_3 = arr_reshape.reshape(2, 3, 2)
print(newarr_reshape_3)
#reshape -> return a view
print(newarr_reshape_3.base)
print("------------------------")




