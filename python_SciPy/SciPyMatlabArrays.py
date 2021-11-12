#exporting data in matlab format
#savemat(): filenames, mdict: a dictionary containing the data,
#           do_compression: a boolean value that specifies whether do compress the result or not: nén hay không

from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#export:
io.savemat('arr.mat', {"vec": arr})
#import:
mydata = io.loadmat('arr.mat')
print(mydata)
