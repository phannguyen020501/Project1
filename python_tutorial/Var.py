x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("--------------------------------")


#global variable
a = "awesome"
def myfunc():
    #biến địa phương
    a = "fantastic"
    print("Python is "+ a)

myfunc()
print("Python is "+ a)
print("--------------------------------")
def myfunc1():
    global b
    b = "fantastic"

myfunc1()
print("Python is "+ b)
print("--------------------------------")
#random number
import  random
print(random.randrange(1,10))
print("--------------------------------")
#Casting number
print(int(2.8)) # -> 2
print(float(3)) # -> 3.0
print(str(3.0)) # -> '3.0'


