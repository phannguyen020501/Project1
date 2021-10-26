#normal distribution is one of most important distributions-> phân phối chuẩn
#using random.normal() method to get a normal data distribution
#3 parameters: loc- where the peak of the bell exists-> trung bình
#scale- how the flat the graph distribution should be-> độ lệch chuẩn
#size the shape of the returned array

#gerenate a random normal distribution of size 2x3
from numpy import  random
x = random.normal(size=(2,3))
print(x)
print("----------------------------")
#generate a random normal distribution of size 2x3. with mean at 1 and standard deviation of 2:
#-> phân phối chuẩn , giá trị trung bình 1, độ lệch chuẩn 2
x = random.normal(loc = 1, scale= 2, size=(2,3))
print(x)
#visualization of normal distribution
import matplotlib.pyplot as plt
import  seaborn as sns

sns.displot(random.normal(size = 1000))
plt.show()
