#viewing the data
#method for getting a quick overview of the DataFrame, head()
#-> return the headers and a specified numbers of rows, starting from the top
import pandas as pd
df = pd.read_csv("data.csv")
print(df.head(10))
print("------------------")
#print the first 5 rows of the DataFrame
print(df.head())
print("------------------------")

#tail(): viewing the last rows of the DataFrame-> 5rows
print(df.tail())
print("------------------------")

#infor about the data: infor() method: gives you more information about the dataset
print(df.info())
print("------------------------")


