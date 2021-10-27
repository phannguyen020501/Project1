#logistic distribution is used to describe growth
#in machine learning in logistic regression, neural networks
#3 parameters: - loc: where is the peak is, default 0.: đỉnh ở đâu
#              - scale: standard deviation, the flatness of distribution: default 1: độ lệch chuẩn, độ phẳng của phân phối
#              - size: the shape of the returned array
from numpy import random
x = random.logistic(loc = 1, scale= 2, size=(2,3))
print(x)

#visualization of logistic distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size = 1000), hist= False)
plt.show()
