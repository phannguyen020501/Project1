#summations
#difference between summations and addition:
#addition is done between two arguments whereas summation happen over n elements

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)#-> [2, 4, 6]
print("-----------------------")
newarr = np.sum([arr1, arr2])
print(newarr)#-> 12
print("-----------------------")
#summation over an axis -> phép cộng qua trục
#if axis = 1, numpy will sum the numbersin each array
newarr = np.sum([arr1, arr2], axis= 1) #-> [6,6]
print(newarr)
print("-----------------------")
#cummulative sum -> tổng tích lũy
#the partial sum of [1, 2, 3, 4] -> [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10]
# use cumsum()
arr = np.array([1, 2, 3, 4, 5])
newarr = np.cumsum(arr)
print(newarr)





