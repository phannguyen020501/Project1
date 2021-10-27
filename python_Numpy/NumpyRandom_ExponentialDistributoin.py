#ExponentialDistribution is used to describing time till next event -> phân phối hàm mũ
#two parameters: -scale:nghịch đảo của tỉ lệ. default: 1.0
#                - size: the shaped of returned size
#example: draw out a sample for exponential distribution with 2.0 scale with 2x3 size
from numpy import random

x = random.exponential(scale=2, size=(2,3))
print(x)

#visualization of expenential distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(size = 1000), hist = False)
plt.show()
