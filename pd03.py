import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"
df = pd.read_csv(url)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print(df["price"].head())
print(df[["carat", "cut", "price"]].head())

expensive = df[df["price"] > 10000]
print(len(expensive), "diamonds cost more than $10,000")

print(df["cut"].value_counts())

print(df.groupby("cut")["price"].mean())

print(df.sort_values("price", ascending=False).head())