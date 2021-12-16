# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX
import time
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		result = []
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])



	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minKey(self, key, mstSet):

		# Initialize min value
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph
	# represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V


		parent[0] = -1 # First node is always the root of

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minKey(key, mstSet)
			# Put the minimum distance vertex in
			# the shortest path tree
			mstSet[u] = True
			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m
				# mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u
		for i in range(self.V):
			if(parent[i] == -1): continue
			print('(',i,',', parent[i],')  ', key[i])

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

	def calculatetime(self):
		start = time.time()
		print("start: ",start)
		self.primMST()
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
		z = []
		for x in data:
			z.append(float(x))
		g.graph.append(z)
	f.close()
	return g



# g = Graph('../Input/input1000.txt')
# t1 = g.calculatetime()
# print("t1: ", t1)
