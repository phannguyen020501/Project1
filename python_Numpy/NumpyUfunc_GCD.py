#GCD: greatest common denominator: bội chung lớn nhất
#also knows as: HCF: highest common factor

#find the hcf of the following 2 numbers:
import numpy as np

num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)#-> 3
print("-----------------------")
#find the gcd in arrays: -> reduce() method
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)#-> 4
print(x)
