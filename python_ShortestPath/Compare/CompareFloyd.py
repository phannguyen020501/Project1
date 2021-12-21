from ScipyFloyd import Graph as graphScipy
from floyd import Graph as graphByMe
filename = "../Input/input.txt"

g1 = graphByMe(filename)
t1 = g1.CalTime()

g2 = graphScipy(filename)
t2 = g2.CalTime()

print("time by me:      ", t1)
print("time by library: ",t2)


