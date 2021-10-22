#hoán vị
from numpy import random
import  numpy as np
#shuffle means changing arrangement of elements in-place
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)
print("-------------------")
#using permutation()
print(random.permutation(arr))
print("-------------------")


