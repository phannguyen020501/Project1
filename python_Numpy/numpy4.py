            #splingting array
#use array_split() for splitting array
import numpy as np
arr = np.array([1, 2, 3, 4 ,5 ,6])
newarr1 = np.array_split(arr, 3)
print(newarr1)
print("----------------------------")
newarr2 = np.array_split(arr, 4)
print(newarr2)
print("----------------------------")
for x in newarr1:
    print(x)
print("----------------------------")
#splitting 2D arrays
#example: split the 2D array into three 2D arrays
arr_2D_1 = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
newarr_2D = np.array_split(arr_2D_1, 3)
print(newarr_2D)
print("----------------------------")
arr_2D_2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
newarr_2D_2 = np.array_split(arr_2D_2,3)
print(newarr_2D_2)
print("----------------------------")
#split 2D array into three 2D arrays along rows
newarr_2D_3 = np.array_split(arr_2D_2, 3, axis = 1)
print(newarr_2D_3)
print("----------------------------")

            #searching arrays
#to search an array, use the where() method
arr_search = np.array([1,2,3,4,5,4,4,2])
x = np.where(arr_search == 4)
print(x)
print("----------------------------")
#find the indexes where the values are even
x = np.where(arr_search%2 == 0)
print(x)
print("----------------------------")
#find the indexes where the values are odd
x = np.where(arr_search%2 == 1)
print(x)
print("----------------------------")
#use searchsorted() -> sort index
x = np.searchsorted(arr )


