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
arr_search_sort = np.array([6,7,8,9])
#find the indexes where value 7 should be inserted
x = np.searchsorted(arr_search_sort, 7)
print(x)
print("----------------------------")
#find the indexes where value 7 should be inserted, starting from the right
x = np.searchsorted(arr_search_sort, 7, side="right")
print(x)
print("----------------------------")
#multiple values-> find the indexes where values 2, 4, 6 should be inserted
x = np.searchsorted(arr, [2,3,4])
print(x)
print("----------------------------")
            #array sort
arr_sort = np.array([3, 2, 0, 1])
print(np.sort(arr_sort))
print("----------------------------")
#can also sort arrays of string or any type
arr_sort_str = np.array(["banana", "cherry", "apple"])
print(np.sort(arr_sort_str))
print("----------------------------")
arr_sort_bln = np.array([True, False, True])
print(np.sort(arr_sort_bln))
print("----------------------------")
#sorting a 2D array
arr_sort_2D = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr_sort_2D))
print("----------------------------")
            #filter array
#if the value at index in True, the ele is contained in the filtered arrays, else that element
#is excluded from the filtered  array
arr = np.array([41,42,43,44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
print("----------------------------")
arr = np.array([1,2,3,4,5,6,7])
filter_arr = arr%2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
