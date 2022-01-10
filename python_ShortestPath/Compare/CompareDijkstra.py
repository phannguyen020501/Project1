from DijkstraSimple import Graph as graphByMe
from ScipyDijkstra import Graph as graphScipy

filename = "../Input/input500.txt"
n =  0

# g1 = graphByMe(filename)
# t1 = g1.calTimeFromNodeN(n)

g2 = graphScipy(filename)
t2 = g2.calTimeFromNodeN(n)

# print("time by me:      ", t1)
print("time by library: ",t2)
