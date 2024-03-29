import sys #for int_max

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("dist:", dist)
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

g = Graph(9)
g.graph =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
g.dijkstra(0)

