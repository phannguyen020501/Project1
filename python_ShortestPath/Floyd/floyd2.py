def initialise(V):
    global dis, Next
    for i in range(V):
        for j in range(V):
            dis[i][j] = graph[i][j]
            #no edge between node i and j
            if( graph[i][j] == INF):
                Next[i][j] = -1
            else:
                Next[i][j] = j
#function construct the shorest path between u and v
def constructPath(u, v):
    global graph, Next

    #if there isnot not path beetween node u and v, simple return an empty array
    if(Next[u][v] == -1):
        return {}

    #sorting the path in a vector
    path = [u]
    while(u != v):
        u = Next[u][v]
        path.append(u)
    return path

#standard floyd warshall that dis[i][j] > dis[i][k] + dis[k][j]
#the we modify next[i][j] = next[i][k]

def floydWarshall(V):
    global dis, Next
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if(dis[i][k] == INF or dis[k][j] == INF):
                    continue
                if(dis[i][j] > dis[i][k] + dis[k][j]):
                    dis[i][j] = dis[i][k] + dis[k][j]
                    Next[i][j] = Next[i][k]

#print the shortest path:
def printPath(path):
    n = len(path)
    distance = 0
    for i in range(n-1):
        print(path[i],end = "->")
        distance = distance + graph[path[i]][path[i+1]]
    print(path[n-1])
    print("tong: ", distance)


def readfileInput(filename):
    f = open(filename, 'r')
    i = 0
    graphdata =[]
    while True:
        data = f.readline().strip()
        if data == '':
            break
        data = data.split(" ")

        z = []
        for x in data:
            if(x != 'INF'):
                z.append((float(x)))
            else:
                z.append(INF)
        graphdata.append(z)
    f.close()
    return graphdata


if __name__== '__main__':
    MAXM, INF = 100, 10**7
    dis = [[-1 for i in range(MAXM)] for i in range(MAXM)]
    Next = [[-1 for i in range(MAXM)] for i in range(MAXM)]

    graph = readfileInput('input2.txt')
    V = len(graph)

    initialise(V)
    floydWarshall(V)
    path =[]
    node = []
    for i in range(V):
        node.append(i)
    while True:
        print("các đỉnh:",node)
        start = input("start: ")
        end = input("end: ")
        path = constructPath(int(start),int(end))
        printPath(path)
        cont = input("tiep tuc: yes/no ")
        if(cont == 'no' or cont != 'yes'):
            break;


