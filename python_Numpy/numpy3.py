            #array iterating
import numpy as np
#iterating arrays
arr1 = np.array([1,2,3])
for x in arr1:
    print(x)
print("----------------------")
#iterating 2-D arrays
arr2 = np.array([[1,2,3],[4,5,6]])
for x in arr2:
    for y in x:
        print(y)
print("----------------------")
#iterating 3-D arrays
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr3:
    for y in x:
        for z in y:
            print(z)
print("----------------------")
#iterating arrays using nditer()
for x in np.nditer(arr3):
    print(x)
print("----------------------")
            #array join
arr_join1 = np.array([1,2,3])
arr_join2 = np.array([4,5,6])
arr_join = np.concatenate((arr_join1,arr_join2))
print(arr_join)
print("----------------------")
#join two 2-D arrays along row(axis = 1)
arr2_join1 = np.array([[1,2],[3,4]])
arr2_join2 = np.array([[5,6],[7,8]])
arr2_join = np.concatenate((arr2_join1,arr2_join2),axis= 1)
print(arr2_join)
print("----------------------")
arr1_join1 = np.array([1,2,3])
arr1_join2 = np.array([4,5,6])
arr1_join = np.stack((arr1_join1, arr1_join2), axis = 1)
print(arr1_join)
print("----------------------")
# stacking along rows
arr_join_row = np.hstack((arr1_join1,arr1_join2))
print(arr_join_row)
print("----------------------")
#stack along columns
arr_join_col = np.vstack((arr1_join1,arr1_join2))
print(arr_join_col)
print("----------------------")
#stack along height(depth)
arr_join_hei = np.dstack((arr1_join1,arr1_join2))
print(arr_join_hei)
