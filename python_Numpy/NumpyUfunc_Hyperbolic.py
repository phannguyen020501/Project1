#hyperbolic functions: sinh(), cosh(), tanh()
import numpy as np
x = np.sinh(np.pi/2)
print(x)
print("----------------------")
#array
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sinh(arr)
print(x)
print("----------------------")
#finding angles: arcsinh(), arccosh(), arctanh()
x = np.arcsinh(1.0)
print(x)
#agles in array
arr = np.array([0.1, 0.2, 0.3])
x = np.arcsinh(arr)
print(x)
