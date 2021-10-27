#rounding decimals -> làm tròn số thập phân
# 5 ways:
#truncation: revome decimals, return the float number closet to zero
import numpy as np
arr = np.trunc([-3.166666, 3.66667])
print(arr)
print("------------------")
arr = np.fix([-3.166666, 3.66667])
print(arr)
print("------------------")
#rounding: increase preceding digit or decimal by 1 if >= 5 else do nothing
#rlàm trong 3.16666 đến 2 chữ số thập phân
arr = np.around(3.16666, 2)
print(arr)
print("------------------")
#floor: round off decimal to nearest lower integer
arr = np.floor([-3.1666, 3.6667])
print(arr)
print("------------------")
#ceil: round off decimal to nearest upper integer
arr = np.ceil([-3.1666, 3.6667])
print(arr)
print("------------------")




