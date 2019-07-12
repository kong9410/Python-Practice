import pandas as pd
d = {'a':(1,101), 'b':(2,202), 'c':(3,303)}
df = pd.DataFrame.from_dict(d, orient="index")
df.to_csv("data.csv")

df = pd.read_csv("data.csv")
d = df.to_dict()

d
