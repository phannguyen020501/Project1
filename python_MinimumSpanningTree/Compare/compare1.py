from KruskalSimple import Graph as GraphKst
from ScipyMST import Graph as GraphScipy
from PrimSimple import Graph as GraphPrim

pathfile ='../Input/input.txt'

g1  = GraphKst(pathfile)
time1 = g1.calculatetime()

g2 = GraphScipy(pathfile)
time2 = g2.calculatetime()

g3 = GraphPrim(pathfile)
time3 = g3.calculatetime()

print("time without library, using kruskal: ", time1)
print("time without library, using prim:    ",time3)
print("time with libarary:                  ", time2)
