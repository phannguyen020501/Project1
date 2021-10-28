#trigonometric functions: hàm lượng giác: sin, cos, tan
import numpy as np
x = np.sin(np.pi/2)
print(x)
print("------------------")
#find the sin value for all the values in arr
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/4])
x = np.sin(arr)
print(x)
print("------------------")
#convert degrees to radius
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
print("------------------")
#convert radius to degree
y = np.rad2deg(x)
print(y)
print("------------------")
#find angles: arcsin(), arccos(), arctan()
x = np.arcsin(1.0)
print(x)
arr = np.array([1, -1, 0.1])
print(np.arcsin(arr))
print("------------------")
#hypotenues: pitago
print(np.hypot(3, 4))

