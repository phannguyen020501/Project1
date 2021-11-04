#pandas uses plot() method to create diagrams
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df.plot()
plt.show()
#Scatter Plot: kind argument, needs x and y-axis

df.plot(kind = "scatter", x = "Duration", y ="Calories")
plt.show()

#Histogram: kind argument: kind = "hist"
#example: will use the "Duration" column to create the histogram
df["Duration"].plot(kind = "hist")
plt.show()
