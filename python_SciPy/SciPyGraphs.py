#working with graphs: module scipy.sparse .csgraph
#adjacency matrix: is an n*n matrix where n is the elements in a graph

#connected components: find all the connected components with the connected_components() method
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
    [0, 1, 2],
    [2, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(arr)
print(connected_components(newarr))
print("---------------------------------------")
#dijkstra: use the dijkstra method to find the shortest path in a group from one element to other
#arguments: return_predecessors: boolean( true to return whole path of traversal otherwise False)
#           indices: index of the element to return all paths from element only
#           limit: max weight of path

from scipy.sparse.csgraph import dijkstra
arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors=True, indices=0))
print(dijkstra(newarr, return_predecessors=False, indices=1))
print("---------------------------------------")

#Floyd warshall: to find shortest path between all pairs of elements
from scipy.sparse.csgraph import floyd_warshall
arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))
print(floyd_warshall(newarr))
print("---------------------------------------")
#bellman ford: find the shortest path between all pairs of elements, but this method can be handle negative weights
#find the shortest path from element 1 and 2 with given graph with negative weight:
from scipy.sparse.csgraph import bellman_ford
arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(arr)
print(bellman_ford(newarr, return_predecessors= True, indices= 0))
print(bellman_ford(newarr,return_predecessors= False, indices= 1))
print("---------------------------------------")

#depth first order: depth_first_order(): method return depth first traversal from a node
from scipy.sparse.csgraph import depth_first_order
arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])

newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))
print("---------------------------------------")
#breadth first order: breadth_first_order(): methods return a breadth first travesal from a node
from scipy.sparse.csgraph import breadth_first_order
arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])

newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))
