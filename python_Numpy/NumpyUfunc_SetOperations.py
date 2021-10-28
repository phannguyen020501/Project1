#  create set in numpy -> unique(): method to find unique elements from any array
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 5, 7])
x = np.unique(arr)
print(x)
print("-------------------------------")
#finding union: union1d() method
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
print("-------------------------------")
#finding intersection : intersect1d() method
newarr = np.intersect1d(arr1, arr2, assume_unique= True)
print(newarr)
print("-------------------------------")
#finding difference: setdiffid() method: the difference set1 from set2
newarr = np.setdiff1d(arr1, arr2, assume_unique= True)
print(newarr)
newarr = np.setdiff1d(arr2, arr1, assume_unique= True)
print(newarr)
print("-------------------------------")
#finding symmetric difference: not present in both sets, setxor1d() method
newarr = np.setxor1d(arr1, arr2, assume_unique= True)
print(newarr)
print("-------------------------------")


