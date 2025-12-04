import pandas as pd

path = "/Users/tyler-barsby/Desktop/coding-fundamentals/Session Tasks/Labs/carSales.csv"

df = pd.read_csv(path, thousands=',')
df = df.set_index('Manufacturer')

print(df.sum(axis=0))
print(df.sum(axis=1))
print(f"Grand total: {df.values.sum()}")