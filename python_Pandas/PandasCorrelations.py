#finding relationships : corr() method: calculates the relationship between each column in data set
import pandas as pd
df = pd.read_csv("data.csv")
print(df.corr())

#result explained: the number varies from -1 to 1
#1 means there is 1 to 1 relationship(a perfect correlation): each time a value went up in the first column, the other one went up as well
#0.9: good relationship, and if you increase one value, the other will probably increase as well
#-0.9: good ralationship as 0.9 but if you increase one value, the other will probably go down
#0.2: mean not a good relationship, meaning if one values goes up does not mean that other will
