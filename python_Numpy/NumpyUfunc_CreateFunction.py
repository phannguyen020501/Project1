#create: define a function, then add it to your Numpy ufunc library with frompyfunc() method:
# frompyfunc(): arguments: - funtion: name of the funtion
#                          - inputs: the number of input arguments(array)
#                          - outputs: the number of output arrays
import numpy as np
def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print("--------------------")
#check if a function is a ufunc -> a ufunc should return <class 'numpy.ufunc'>
print(type(np.add))
print("--------------------")

if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")

