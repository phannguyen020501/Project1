from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

class Graph:
    def __init__(self, verticies):
        self.V = verticies  #no of vertices
        self.graph = []     #default dictionary
    #function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

def readFileInput(filename):
    f = open(filename, 'r')
    n = int(f.readline())
    g = Graph(n)
    i = 0
    datagraph = []
    while True:
        data = f.readline().strip()
        if data == '':
            break
        data = data.split(" ")
        z = []
        for i in range(n):
            z.append(float(data[i]))
        datagraph.append(z)
    f.close()
    g.graph = csr_matrix(datagraph)
    return g

g = readFileInput("../Input/input.txt")
Tcsr = minimum_spanning_tree(g.graph)
print(Tcsr)
