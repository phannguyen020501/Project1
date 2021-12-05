# Number of vertices
nV = 4
INF = 999
import numpy as np
# Algorithm
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def floyd(self):
        dist = list(map(lambda p: list(map(lambda q: q, p)), self.graph))


        # Adding vertices individually
        for r in range(self.V):
            for p in range(self.V):
                for q in range(self.V):
                    if(dist[p][q] > dist[p][r] + dist[r][q]):
                        dist[p][q] = dist[p][r] + dist[r][q]

        self.sol(dist)


    # Printing the output
    def sol(self, dist):
        for p in range(self.V):
            for q in range(self.V):
                if(dist[p][q] == INF):
                    print("INF", end=" ")
                else:
                    print(dist[p][q], end="  ")
            print(" ")


g = Graph(4)
g.graph = [[0, 5, INF, INF],
         [50, 0, 15, 5],
         [30, INF, 0, 15],
         [15, INF, 5, 0]]
g.floyd()
