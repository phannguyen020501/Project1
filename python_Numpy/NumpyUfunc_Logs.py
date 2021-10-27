#logs: log at base 2, e, 10

import numpy as np
#log at base 2:
#example find log at base 2 of all elements
arr = np.arange(1, 10)
print(np.log2(arr))
print("---------------------")
#log at base10:
print(np.log10(arr))
print("------------------")
#natural log or log at base e:
print(np.log(arr))
print("------------------")
#log at any base: numpy does provide any function to take log at any base: so we can use frompyfunc()
from math import log
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))# log15(100)

