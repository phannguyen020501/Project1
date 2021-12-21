from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


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
def printpath(start, end, predecessor):
    stack = []
    stack.append(end)
    while(start != end):
        z = int(predecessor[start][end])
        end = z
        stack.append(z)
    size = len(stack)
    for j in range(size):
        print(stack.pop() ,end = " ")
    print()

g = readFileInput('../Input/input1000.txt')
V = len(g.graph)
node = []
for i in range(V):
    node.append(i)
graph =csr_matrix(g.graph)
dist_matrix , predecessors= floyd_warshall(csgraph= graph, return_predecessors= True)
while True:
    print("các đỉnh:",node)
    start = int(input("start: "))
    end = int(input("end: "))
    printpath(start, end, predecessors)
    print("tổng = ", dist_matrix[start][end])
    cont = input("tiep tuc: yes/no ")
    if(cont == 'no' or cont != 'yes'):
        break;

