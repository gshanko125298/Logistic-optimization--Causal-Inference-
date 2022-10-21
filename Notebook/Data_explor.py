import datashader as ds, pandas as pd, colorcet as cc

df = pd.read_csv('C:\Users\Genet Shanko\Logistic_optim_Data\nb.csv', usecols=['dropoff_x', 'dropoff_y'])
df.head()