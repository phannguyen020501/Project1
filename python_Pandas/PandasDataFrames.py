#pandas dataframe: 2 dimensional data structures, like 2D array, or a table with rows and columne
#create simple pandas dataframes
import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
#load data into a dataframe object
df = pd.DataFrame(data)
print(df)
print("------------------------")
#locate row: loc() -> hàng
print(df.loc[0])
print("--------------------------")
#return row 0 and 1 -> use list of indexes
print(df.loc[[0,1]])
print("--------------------------")
#named indexes
df = pd.DataFrame(data, index= ["day1", "day2", "day3"])
print(df)
print("--------------------------")
#locate named index -> loc() -> return row(s) : hàng
print(df.loc["day2"])
#load files into a dataFrame
df = pd.read_csv('data.csv')
print(df)
