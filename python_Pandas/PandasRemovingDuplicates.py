#duplicates: have been registered more than one time
#to discover duplicates, use duplicated() method: -> return Boolean value for each rows
import pandas as pd
data = {
    "Duration": [60, 60, 60, 60],
    "Date":["2020/12/12","2020/12/12","2020/12/13","2020/12/14"],
    "Calories":[500, 500, 501, 502]
}
df = pd.DataFrame(data)
print(df)
print("----------------------------------")
#duplicated()
print(df.duplicated())
print("----------------------------------")
#remove duplicated()-> use drop_duplicates() method
df.drop_duplicates(inplace= True)
print(df)
print("----------------------------------")


