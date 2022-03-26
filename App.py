from numpy import delete
import pandas as pd
import csv

df = pd.read_csv('planet.csv')
print(df.shape)

del df["Luminosity"]
del df["Drawf Star Name"]
del df["Dist"]
del df["Weight"]
del df["Rad"]
del df['Unnamed']

df.to_csv('stars.csv')