#data of wrong format: to fix it, 2 options: remove the rows, or convert the cells
#convert:
#convert date: to_datetime()
import pandas as pd
data = {
    "date":["2020/12/01","2020/12/02","20201203"],
    "calories":[500, 501, 499]
}
df = pd.DataFrame(data)
print(df)
print("-------------------------------------------")
#convert:
df["date"] = pd.to_datetime(df["date"])
print(df.to_string())
