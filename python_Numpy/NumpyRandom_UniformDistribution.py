#uniform distribution -> phân phối đều
#used to describe probability where every events has equal chances of occuring
#3 parameters:- a :lower bound . default 0.0
#             - b: upper bound . default 1.0
#             - size: the shape of returned array
#create 2x3 uniform distribution sample
from numpy import  random
x = random.uniform(size=(2,3))
print(x)
#visualazation of uniform distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size= 1000), hist=False)
plt.show()
