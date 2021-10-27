#simple arithmetic: số học đơn giản
#addition: add() -> function sums of the content of 2 array, return new arr
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
print("-------------------------------")
#substract : substract()
newarr = np.subtract(arr1, arr2)
print(newarr)
print("-------------------------------")
#multiply: multiply()
newarr = np.multiply(arr1, arr2)
print(newarr)
print("-------------------------------")
#divide: divide()
newarr = np.divide(arr1, arr2)
print(newarr)
print("-------------------------------")
#power: power() -> mũ
arr3 = np.array([1,2,3,4,5,6])
newarr = np.power(arr1, arr3)
print(newarr)
print("-------------------------------")
#mod: chia số dư
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)
newarr = np.remainder(arr1, arr2) #-> same rs: mod
print(newarr)
print("-------------------------------")
#divmod:
newarr = np.divmod(arr1, arr2)
print(newarr)
print("-------------------------------")
#absolute values: absolute: trị tuyệt đối
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
