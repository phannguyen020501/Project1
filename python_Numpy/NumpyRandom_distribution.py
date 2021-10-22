#data distribution is a list of all possible values, and how to often each values occurs
#->using choice() method
from numpy import random
#generate 1D arrays containing 100 values, where each values has to be 3,5,7,9: 0.1;0.3;0.6;0
x = random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
print("------------------")
#same example but return 2D arrays size(3,5)
x = random.choice([3,5,7,9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print(x)
print("------------------")


