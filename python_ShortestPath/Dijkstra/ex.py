# GUI based implementation of Dijkstra's algorithm
import sys
import networkx as nx
import matplotlib.pyplot as plt


# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = sys.maxsize
        self.parent = None
        self.parentEdgeWeight = None

    def add_neighbor(self, neighbor, weight):
        if (neighbor not in self.neighbors):
            self.neighbors[neighbor] = weight
        else:
            print(neighbor + ' is already a neighbor of ' + self.name + '!')

    def print_neighbors(self):
        print('printing all neighbors and their respective weights...')
        for n, w in self.neighbors.items():
            print('neighbor: ' + n + 'weight: ' + w)


# Graph class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name):
        if (name not in self.graph):
            newNode = Node(name)
            self.graph[name] = newNode
        else:
            print('node ' + name + ' already exists!')

    def add_edge(self, u, v, w):
        if (u in self.graph and v in self.graph):
            self.graph[u].add_neighbor(v, w)
        else:
            print('error adding edge between ' + u + ' and ' + v +
                  '! check that both nodes exist in the graph...')

    def print_graph(self):
        print('printing graph...')
        for u, u_node in self.graph.items():
            print(u + ': ' + str(u_node.neighbors))

    def Dijkstra(self, s):

        # check that starting node exists in the graph
        if (s not in self.graph):
            print('node with name ' + s + ' does not exist in the graph!')
            return

        # init distance of source node and build unvisited minheap
        self.graph[s].distance = 0
        unvisited = MinHeap(self.graph)

        while (unvisited.currSize > 0):

            current_node = unvisited.getMin()

            # check if its neighbors can do any better by using one of its edges
            for n, w in current_node.neighbors.items():

                if (self.graph[n].distance > current_node.distance + w):
                    self.graph[n].distance = current_node.distance + w
                    self.graph[n].parent = current_node.name
                    self.graph[n].parentEdgeWeight = w
            unvisited.extract()

        for u, v in self.graph.items():
            print('shortest distance from ' + s +
                  ' to ' + u + ': ' + str(v.distance))


# MinHeap class
class MinHeap:
    def __init__(self, graph):
        self.maxSize = len(graph)
        self.currSize = 0

        # build heap
        self.heap = [Node('dummyNode')] * (self.maxSize + 1)
        self.heap[0].distance = -1 * sys.maxsize
        self.min = 1

        for v in graph.values():
            self.insert(v)
        for pos in range(self.currSize//2, 0, -1):
            self.heapify(pos)

    def getParent(self, elt):
        return elt // 2

    def getLeftChild(self, elt):
        return elt * 2

    def getRightChild(self, elt):
        return (elt * 2) + 1

    def isLeaf(self, elt):
        if (elt <= self.currSize) and (elt >= self.currSize // 2):
            return True
        else:
            return False

    def swap(self, elt1, elt2):
        self.heap[elt1], self.heap[elt2] = self.heap[elt2], self.heap[elt1]

     # insert an element into the heap
    def insert(self, elt):
        if (self.currSize == self.maxSize):
            return
        self.currSize += 1
        self.heap[self.currSize] = elt

        currElt = self.currSize

        while (self.heap[self.getParent(self.currSize)].distance > self.heap[currElt].distance):
            self.swap(self.getParent(self.currSize), currElt)
            currElt = self.getParent(currElt)

    def heapify(self, elt):

        if self.currSize == 0:
            return

        if (self.isLeaf(elt)):
            return
        if (self.heap[elt].distance > self.heap[self.getLeftChild(elt)].distance or
                self.heap[elt].distance > self.heap[self.getRightChild(elt)].distance):

            # swap elt with smaller child and recurse
            smallerChild = self.getLeftChild(elt)
            if (self.heap[self.getRightChild(elt)].distance < self.heap[smallerChild].distance):
                smallerChild = self.getRightChild(elt)

            self.swap(elt, smallerChild)
            self.heapify(smallerChild)

    # extract minimum element from the heap
    def extract(self):
        self.heap[self.min] = self.heap[self.currSize]
        self.currSize -= 1
        self.heapify(self.min)

    def getMin(self):
        return self.heap[self.min]


def main():

    print('*********************************************')
    print('n: add a node')
    print('e: add an edge')
    print('g: see the graph as it currently stands')
    print('d: run Dijkstra\'s algorithm')
    print('x: exit program')
    print('*********************************************')

    # initialize graph
    g = Graph()

    # prompt user
    while True:
        action = input('please select an action: ')

        if action == 'n':
            nodeName = input('please enter a unique node name: ')

            if nodeName in g.graph:
                print('node with that name already exists...')
                continue
            g.add_node(nodeName)
        elif action == 'e':
            fromNode = input('coming from: ')
            if fromNode not in g.graph:
                print('node does not exist!')
                continue
            toNode = input('and going to: ')
            if toNode not in g.graph:
                print('node does not exist!')
                continue
            weight = input('with edge weight (no negative numbers!): ')
            try:
                weight = float(weight)
            except ValueError:
                print('invalid weight!')
                continue
            if weight < 0:
                print('no negative weights allowed!')
                continue
            g.add_edge(fromNode, toNode, weight)
        elif action == 'g':
            if len(g.graph) == 0:
                print('there are no nodes in the graph!')
                continue

            DG = nx.DiGraph()

            for u in g.graph.keys():
                DG.add_node(u)

            for u, v in g.graph.items():
                for n, w in v.neighbors.items():
                    DG.add_edge(u, n, weight=w)

            # draw graph
            pos = nx.random_layout(DG)
            nx.draw(DG, pos, with_labels=True)
            labels = nx.get_edge_attributes(DG, 'weight')
            nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels)
            plt.draw()
            plt.show()

        elif action == 'd':
            start = input('node to run Dijkstra\'s algorithm from: ')

            if start not in g.graph:
                print('node does not exist in the graph...')
                continue

            g.Dijkstra(start)

            DG = nx.DiGraph()

            for u in g.graph.keys():
                DG.add_node(u)

            for u, v in g.graph.items():
                if (v.parent != None):
                    DG.add_edge(v.parent, u, weight=v.parentEdgeWeight)

            # draw graph
            pos = nx.random_layout(DG)
            nx.draw(DG, pos, with_labels=True)
            labels = nx.get_edge_attributes(DG, 'weight')
            nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels)
            plt.draw()
            plt.show()

        elif action == 'x':
            return
        else:
            print('invalid action! try again!')


if __name__ == "__main__":
    main()
