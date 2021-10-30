import pandas as pd
mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
print("--------------------------")
#cheking pandas version
print(pd._version)
print("--------------------------")


