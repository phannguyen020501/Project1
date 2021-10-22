#pseudo random and true random
from numpy import random
x = random.randint(100)
print(x)
print("-------------------------")
#rand() methods returns a random float between 0 and 1
x = random.rand()
print(x)
print("-------------------------")
#generate random array
#generate 1D array containing 5 random int from 0 to 100
x = random.randint(100, size=(5))
print(x)
print("-------------------------")
#generate 1D array containing 5 random floats
x = random.rand(5)
print(x)
print("-------------------------")
#generate 2D array with 3 rows, each row containing 5 random numbers
x = random.rand(3, 5)
print(x)
print("-------------------------")
#generate random number from array-> using choice()
x = random.choice([3, 5, 7, 9])
print(x)
#choice method also allows to return an arrays of values
#size-> shape of array
x = random.choice([3, 5, 7, 9], size=(3,5))
print(x)
#random
