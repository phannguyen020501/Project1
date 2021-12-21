import time

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def __init__(self, filename):
        f = open(filename, 'r')
        n = int(f.readline())
        self.V = n
        self.graph = []
        i = 0
        while True:
            data = f.readline().strip()
            if data == '':
                break
            data = data.split(" ")
            z = []
            for x in data:
                z.append(float(x))
            self.graph.append(z)
        f.close()
    def printShortestResult(self, n):
        graph = csr_matrix(self.graph)
        dist_matrix , predecessors= dijkstra(csgraph= graph, return_predecessors= True)
        for i in range(self.V):
            print(n,"-",i," ",dist_matrix[n][i])
    def calTimeFromNodeN(self, n):
        start = time.time()
        print("start ", start)
        self.printShortestResult(n)
        end = time.time()
        print("end ", end)
        return end-start



# g = Graph('../Input/input1000.txt')
# print(g.calTimeFromNodeN(0))
