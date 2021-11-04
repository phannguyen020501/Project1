#empty cells: can potentially give you a wrong result when you analyze data
#remove cells:
import pandas as pd
df = pd.read_csv("dirtydata.csv")
new_df = df.dropna()
print(new_df.to_string())#-> return a new  Dataframe with no empty cells
print("---------------------------")
#remove all rows with NULL value: use the inplace = True argument
df1 = pd.read_csv("dirtydata.csv")
df1.dropna(inplace = True)
print(df1.to_string())
print("---------------------------")
#replace empty values: fillna() method
#replace NULL values with the number 130
df2 = pd.read_csv("dirtydata.csv")
df2.fillna(130, inplace= True)
print(df2.to_string())
print("---------------------------")
#replace only for a specified columns
df3 = pd.read_csv("dirtydata.csv")
df3["Calories"].fillna(130, inplace = True)
print(df3.to_string())
print("---------------------------")
#replace using Mean, Median or Mode: a common way to replace empty cells, is to calculate the mean, median, mode value
df4 = pd.read_csv("dirtydata.csv")
x = df4["Calories"].mean()
df4["Calories"].fillna(x, inplace = True)
print(df4.to_string())
#mean: the average value
#meidan: the value in the middle
#mode: the value that appears most frequently
print("---------------------------")



