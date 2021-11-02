import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
print("------------------------")
#by default: print dataframe, will only get the first 5rows and the last 5 rows
print(df)
