#Scipy Optimizers: tìm giá trị tối ưu của hàm
#Roots of function : numpy is capable of finding roots for polynomials and linear equations but it can not
#find roots for non linear equations: function: optimze.root: 2 required arguments:
# fun: a function representing an equation , x0: an initial guess for the root

#find the root of equation: x + cos(x)
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)
print(myroot.x)
print("----------------------------")
#print all information about the solution
print(myroot)
print("----------------------------")

#minimizing a function: we can use scipy.optimize.minimize()
#following arguments: fun: a function representing an equatoin
#                     x0: an initial guess for the root
#                     method: name of method to use: CG, BFGS, Newton-CG, L-BFGS-B, TNC, COBYLA, SLSQP
#                     callback: function called after each iteration of optimization
#                     options: a dictionnary defining extra params

#example: minize the function: x^2 + x + 2 with BFGS
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn, 0, method="BFGS")
print(mymin)
print("----------------------------")

