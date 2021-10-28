#difference: substracting 2 successive elements
#eg: for[1, 2, 3, 4]: the discrete difference would be: [2-1, 3-2, 4-3] = [1, 1, 1]
#using : diff()
import numpy as np
arr = np.array([10 ,15, 25, 5]) #-> [15-10, 25-15, 5-25]
newarr = np.diff(arr)
print(newarr)
print("------------------------")

#we can perform this operation repeatedly by giving parameter n
#[1, 2, 3, 4] n = 2. would be: [1-2, 2-3, 3-4] = [1, 1, 1]. then [1-1, 1-1] = [0, 0]
newarr= np.diff(arr, n = 2) #-> [5, 10, -20] -> [-5, 30]
print(newarr)
print("------------------------")


