from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib
#class to represent a graph
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
            print("edged in the construct MST")
            for u, v, weight in result:
                mininumCost += weight
                print("%d -- %d == %d" %(u, v, weight))
            print("Mininum Spanning Tree", mininumCost)
            print("result = ",result)
        return result

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



g = readFileInput("../Input/input2.txt")
rs = g.KruskalMST()
dGraph(g.graph)
#dGraphUpdate(g.graph, rs)
