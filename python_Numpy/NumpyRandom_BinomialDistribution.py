#binomial distribution -> phân phối nhị thức
#three parameters:
#n - number of trials -> số lần thử
#p - probability of occurence of each trial-> xác suất
#size - the shape of the returned array
#example given 10 trials for coin toss generate 10 data points
from numpy import random
x = random.binomial(n = 10, p = 0.5, size=10)
print(x)

#visualization of binomial distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n =10, p=0.5, size=1000), hist = True, kde=False)
plt.show()
