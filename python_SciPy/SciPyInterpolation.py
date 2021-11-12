#interpolation: is a method for generating point between given points
#for points 1 and 2: 1.33, 1.66
#1D Interpolation: nội suy
#example: for given xs and ys interpolation values from 2.1, 2.2, ... to 2.9

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
print(xs)
ys = 2*xs + 1
print(ys)
interp_func = interp1d(xs, ys)
print(interp_func)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
