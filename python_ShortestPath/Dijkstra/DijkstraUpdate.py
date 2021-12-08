import sys #for int_max
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printSolution(self, dist):
        print("Vertex \t Distance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])
    #a utility function to find the vertex with minimum distance value
    #from the set of vertices not yet included in shortest path tree

    def minDistance(self, dist, sptSet):
        #init minimum distance for next node
        min = int(sys.maxsize)

        #search for the nearest vertex not in the shortest path tree
        for u in range(self.V):
            if(dist[u] < min and sptSet[u] == False):
                min = dist[u]
                min_index = u
        return min_index

    #function that implements dijkstra's single source shortest path algo for a graph represented
    #using adjacency matrix representation

    def dijkstra(self, src):
        dist = [sys.maxsize]*self.V
        dist[src] = 0
        sptSet = [False]*self.V

        for count in range(self.V):
            #pick the minimum distance vertex from the set of vertices not yet processed
            #x is always equal to src in first iteration:
            x = self.minDistance(dist, sptSet)

            #put the minimum distance vertex in the shortest path tree
            sptSet[x] = True

            #update dist value of adjacent vertices of the picked vertex only if the current
            #distance is greater than new distance and the vertex in not in the shortest path tree

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)
def readFileInput(filename):
    f = open(filename, 'r')
    n = int(f.readline())
    g = Graph(n)
    i = 0
    while True:
        data = f.readline().strip()
        if data == '':
            break
        data = data.split(" ")

        z = []
        for x in data:
            z.append((float(x)))
        g.graph.append(z)
    f.close()
    return g

g = readFileInput('../Input/input.txt')
print(g.graph)
g.dijkstra(1)



