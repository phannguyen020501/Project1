#ufuncs stand for "unviersal Fucntions" -> ndarray object
#ufuncs: khai hóa vecto trong Numpy, cách này nhanh hơn lặp lại phần tử
#ufuncs: take additional arguments, like:
#       where: boolean array or condition defining where the operation should be take place
#       dtype: defining the returns type of elements
#       out:  output array where the return value should be copied

#exmaple: without ufunc, use python zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x,y):
    z.append(i + j)
print(z)
print("------------------")
#numpy has a ufuncs for this call add(x, y)
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
print("------------------")




