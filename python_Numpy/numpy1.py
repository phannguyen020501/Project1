import numpy as np
            #check numpy version
print(np.__version__)
print("----------------------------")
            #create array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
#0-D array
arr0 = np.array(42)
print(arr0)
#1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
#2-D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
#3-D array
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)
print("----------------------------")
#check numper of dimensions
print("arr:",arr0.ndim)
print("arr1:",arr1.ndim)
print("arr2:",arr2.ndim)
print("arr3:",arr3.ndim)
print("----------------------------")
#higher dimensional array
arr5 = np.array([1,2,3,4,5], ndmin = 5)
print(arr5)
print("number of dimension is:",arr5.ndim)
print("----------------------------")

            #array indexing
#access array elements
print("first ele",arr[0])
print("second ele", arr[1])
print("----------------------------")
#access 2-D arrays
arr_indexing_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("2nd element on 1st dim", arr_indexing_2[0, 1])
print("5th element on 2nd dim", arr_indexing_2[1, 4])
print("----------------------------")
#access 3-D arrays
arr_indexing_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_indexing_3[0,1,2])
print("----------------------------")
            #array slicing
#syntax: [start:end] or [start:end:step]
arr_sclicing_1 = np.array([1,2,3,4,5,6,7])
#slice element from index 1 to 5
print(arr_sclicing_1[1:5])
#index 4 to the end
print(arr_sclicing_1[4:])
#from the beginning to index 4(not included)
print(arr_sclicing_1[:4])
#step
print(arr_sclicing_1[1:5:2])
print(arr_sclicing_1[::2])
print("----------------------------")
arr_sclicing_2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#second dim, slice ele from 1 to 4 (not included)
print(arr_sclicing_2[1,1:4])
#from both dim, return index 2
print(arr_sclicing_2[0:2,2])
#form both dim, slice index 1 to 4(not included)->return 2Darray
print(arr_sclicing_2[0:2, 1:4])




