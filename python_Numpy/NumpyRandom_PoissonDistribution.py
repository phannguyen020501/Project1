#poisson distribution -> phân phối poisson
#-> it estimates how many times an event can happen in a specified time
#2 parameters: lam- rate or  known number of occurences -> tỉ lệ hoặc số lần xuất hiện
#                 - size: the shape of the returned array
from numpy import  random
x = random.poisson(lam = 2, size = 10)
print(x)

#visualization of poisson distribution
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam = 2, size = 1000), kde = False)
plt.show()
