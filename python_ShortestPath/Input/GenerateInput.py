import numpy as np

N = 5000
b = np.random.randint(0,2000,size=(N,N))

for i in range(N):
    b[i][i] = 0

print(b)

f = open('input5000.txt',"w")
f.writelines(str(N)+'\n')
for i in range(N):
    for j in range(N):
        f.write(str(b[i][j])+' ')
    f.write('\n')
