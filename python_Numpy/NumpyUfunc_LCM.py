#LCM: lowest common multiple : bội chung nhỏ nhất
#find the LCM of 2 numbers:

import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
print("-----------------------")

#find the lcm in arrays -> use: reduce()
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr) #-> 18
print(x)
print("-----------------------")
#example: find the lcm of an array where the array contains all integers from 1 to 10
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
