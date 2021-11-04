import pandas as pd

data = {
    "duration":[60,600,60,70],
    "date":["2020/12/01","2020/12/02","20201203","20201204"],
    "calories":[500, 501, 499,502]
}
df = pd.DataFrame(data)
print(df)
print("---------------------")
#row 1: duration must be 60
#change-> loc
df.loc[1, "duration"] = 60
print(df)
print("---------------------")
#delete row where duration higher than 60
for x in df.index:
    if df.loc[x, "duration"] > 60:
        df.drop(x, inplace= True)

print(df)
print("---------------------")

