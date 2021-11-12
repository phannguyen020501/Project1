#scipy spatial data: refers to data that is represented in geometric space: không gian hình học
#eg: point on coordinate system
#triangulation: tam giác: chia đa giác thành nhiều tam giác
"""import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])

simplices = (Delaunay(points).simplices)
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

#plt.show()
"""

#convex hull: the smallest polygon that covers all of the given points
"""import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0],points[:, 1])
for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.show()
"""
#KDTrees: are a datastructure optimized for nearest neighbor queries
#find the nearest neighbor to point (1, 1)
from scipy.spatial import KDTree
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)
print("----------------------------------")
#Distance matrix
#Euclidean distance:
from scipy.spatial.distance import euclidean
p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)
print("----------------------------------")
#cityblock distance(manhattan distance): is the distance computed using 4 degrees of movement
from scipy.spatial.distance import cityblock
p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)
print("----------------------------------")
#cosine distance
from scipy.spatial.distance import cosine
p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)
print("----------------------------------")
#hamming distance: is the proportion of bits where two bits are difference
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)
print("----------------------------------")


