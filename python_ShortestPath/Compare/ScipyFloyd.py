import time

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

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
    def printShortestResult(self):
        graph = csr_matrix(self.graph)
        dist_matrix , predecessors= floyd_warshall(csgraph= graph, return_predecessors= True)
        print(dist_matrix)
    def CalTime(self):
        start = time.time()
        print("start ", start)
        self.printShortestResult()
        end = time.time()
        print("end ", end)
        return end-start



# g = Graph('../Input/input1000.txt')
# print(g.calTimeFromNodeN(0))
