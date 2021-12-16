import numpy as np

N = 5000
b = np.random.randint(0,2000,size=(N,N))
b_symm = (b + b.T)/2

for i in range(N):
    b_symm[i][i] = 0

print(b_symm)

f = open('input5000.txt',"w")
f.writelines(str(N)+'\n')
for i in range(N):
    for j in range(N):
        f.write(str(b_symm[i][j])+' ')
    f.write('\n')
