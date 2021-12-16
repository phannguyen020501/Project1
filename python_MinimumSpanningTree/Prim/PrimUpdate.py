import sys #library for int_max
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printMST(self, parent):
        print("Edge \t Weight")
        result = []
        for i in range (1, self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
            result.append([parent[i], i, self.graph[i][ parent[i]]])
        return result

    def minkey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize]*self.V
        parent = [None]*self.V

        key[0] = 0
        mstSet = [False]*self.V

        parent[0] = -1
        for count in range(self.V):
            u = self.minkey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        rs = self.printMST(parent)
        print("result = ", rs)
        return rs

def dGraph( listMST ):
    #Creating Graph to image
    G = nx.Graph()

    #Recursive Function to adding Edge
    for i in range( len( listMST ) ):
        G.add_edge( listMST[i][0], listMST[i][1], weight = float( listMST[i][2] ))
    edge=[( u,v ) for ( u,v,d ) in G.edges( data=True )]
    print(edge)

    #Formatting Nodes Position
    position=nx.spring_layout( G, k=20, pos=None, fixed=None, iterations=150, weight='weight', scale=1.0 )

    #Reading Weight Edge
    weight = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['weight'] ) ), G.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(G, position, edge_labels = weight)

    #Find the longest node name

    #Drawing Nodes Function
    nx.draw_networkx_nodes( G, position, node_size=180,  node_color='#cc0c38' ,node_shape='o', alpha=0.5 )

    #Drawing Edges Function
    nx.draw_networkx_edges( G, position, edgelist=edge, width=2, edge_color='black', alpha=0.5 )

    #Drawing Labels
    nx.draw_networkx_labels( G, position, font_size=9, font_family='sans-serif' )

    #Plotting using Matplotlib
    plt.axis('off')
    plt.show()
def dGraphUpdate(listDT, listMST ):
    #Creating Graph to image
    G = nx.Graph()
    #Recursive Function to adding Edge
    for i in range( len( listDT ) ):
        G.add_edge( listDT[i][0], listDT[i][1], weight = float( listDT[i][2] ))
    edge=[( u,v ) for ( u,v,d ) in G.edges( data=True )]
    edgeMST = []
    rsMST = 0
    for i in range( len( listMST ) ):
        x = listMST[i][0]
        y = listMST[i][1]
        w = float(listMST[i][2] )
        rsMST+=w
        z = (x, y)
        edgeMST.append(z)
    print(edgeMST)
    print(edge)

    #Formatting Nodes Position
    position=nx.spring_layout( G, k=20, pos=None, fixed=None, iterations=150, weight='weight', scale=1.0 )

    #Reading Weight Edge
    weight = dict( map( lambda x:( ( x[0],x[1] ), str( x[2]['weight'] ) ), G.edges( data = True ) ) )
    nx.draw_networkx_edge_labels(G, position, edge_labels = weight)

    #Find the longest node name

    #Drawing Nodes Function
    nx.draw_networkx_nodes( G, position, node_size=180,  node_color='#cc0c38' ,node_shape='o', alpha=0.5 )

    #Drawing Edges Function
    nx.draw_networkx_edges( G, position, edgelist=edge, width=0.5, edge_color='gray', alpha=0.5 )
    nx.draw_networkx_edges( G, position, edgelist=edgeMST, width=2, edge_color='red', alpha=0.5 )

    #Drawing Labels
    nx.draw_networkx_labels( G, position, font_size=9, font_family='sans-serif' )

    strMST = "MST = "+ str(rsMST)

    plt.text(-1, -1,strMST)    #Plotting using Matplotlib
    plt.axis('off')
    plt.show()

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
            z.append(float(x))
        g.graph.append(z)
    f.close()
    return g


g = readFileInput("../Input/input3.txt")
print("graph = ",g.graph)
rs = g.primMST()

graphdata = []
for i in range(g.V-1):
    j = i + 1
    while j < g.V:
        graphdata.append([i, j, g.graph[i][j]])
        j = j+1
dGraphUpdate(graphdata, rs)


