#what is sparse data: is data that has mostly unused elements
#It can be an array like this one: [1, 0, 2, 0, 0 , 3, 0 , 0 , 0 , 0]
#sparse data: data set where most of the item values are zero
#dense data: is the opposit of a sqarse data: most of the values are not zero

#how to work with sparse data: module: scipy.sqarse
#CSC: compressed sparse column
#CSR: compressed sparse row

#CSR matrix:
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
#return (0, 5) 1: items in row 0 position 5 and has the value 1
#       (0, 6) 1: items in row 0 position 6 and has the value 1
#       (0, 8) 2: items in row 0 position 8 and has the value 2
print("-------------------------------------")

#sparse matrix methods: viewing stored data(not the zero items) with the data property:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)
print(csr_matrix(arr).count_nonzero())#-> return 3
print("-------------------------------------")

#remove zero-entries from the matrix with eliminate_zeros() method:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)
print("-------------------------------------")
#eliminating duplicate entries with the sum_duplicates() method:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)
print("-------------------------------------")
#converting from csr to csc with the tocsc() method
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)
