# Number of vertices
import time

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
    def __init__(self, filename):
        f = open(filename, 'r')
        self.V = int(f.readline())
        i = 0
        self.graph = []
        i = 0
        while True:
            data = f.readline().strip()
            if data == '':
                break
            data = data.split(" ")
            z = []
            j = 0
            for x in data:
                if(float(x) == 0 and i != j):
                    z.append(INF)
                else:
                    z.append(float(x))
                j = j+1
            self.graph.append(z)
            i = i+1
        f.close()

    def CalTime(self):
        start = time.time()
        print("start ", start)
        self.floyd()
        end = time.time()
        print("time ", end)
        return end - start

g = Graph("../Input/input.txt")
print(g.CalTime())
