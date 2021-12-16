import time
class Graph:
    def __init__(self, verticies):
        self.V = verticies  #no of vertices
        self.graph = []     #default dictionary
    #function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])


    #utility function to find set of element i// tìm gốc của 1 đỉnh// 1 đỉnh là gốc khi parent là chính nó
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #function that does union of two sets of x anh y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        #attach smaller rank tree under root of high rank tree (union by rank)
        if(rank[xroot] < rank[yroot]):
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #if ranks are same, then make one as root
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    #the main function
    def KruskalMST(self):
        result = [] #this will store the resultant MST
        #an index variable, used for stored edges
        i = 0
        #an index variable, used for result[]
        e= 0

        #Step1: sort all the edges
        self.graph = sorted(self.graph, key= lambda item: item[2])

        parent = []
        rank = []
        #create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        #number of edges to be taken is equal to V-1
        while e < self.V - 1:
            #step 2: pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            #if including this edges doest cause cycle, include it in result, and increment the index result for the next edges
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                #else discard the edges

            mininumCost = 0
            for u, v, weight in result:
                mininumCost += weight
        for u, v, weight in result:
            print(u, "- ", v,": ", weight)
        print("Mininum Spanning Tree", mininumCost)

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
            j = i +1
            while j < int(n):
                w = float(data[j])
                if w != 0:
                    self.addEdge(i, j , w)
                j= j +1
            i = i + 1
        f.close()
    def calculatetime(self):
        start = time.time()
        print("start: ",start)
        self.KruskalMST()
        end = time.time()
        print("end: ", end)
        return end-start
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
        j = i +1
        while j < int(n):
            w = float(data[j])
            if w != 0:
                g.addEdge(i, j , w)
            j= j +1
        i = i + 1
    f.close()
    return g

# g = Graph('../Input/input.txt')
# g.calculatetime();

