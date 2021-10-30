#series: like a column in a table, it is one-dimensional array holding data of any type
#create a simple Pandas series from a list

import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print("--------------------------")
#label: first values has index 0, second values index 1, etc
print(myvar[0])
print(myvar[1])
print(myvar[2])
print("--------------------------")
#create label: index argument
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print("--------------------------")
print(myvar["x"])
print(myvar["y"])
print(myvar["z"])
print("--------------------------")
#key/ values objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
print("--------------------------")
#create a series using only data from "day1" and "day2"
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
print("--------------------------")
#data frames: data sets in pandas are usually multi-dimensional tables, called DataFrames
#series like a column, dataframe is the whole table
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
print("--------------------------")

