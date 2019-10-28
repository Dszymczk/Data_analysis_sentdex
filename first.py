import pandas as pd

df = pd.read_csv("datasets/avocado.csv")

# print(df.head(3)) # shows 3 first elements
# print(df.tail(2)) # showes 2 last elements
# print(df["AveragePrice"].head()) # prints only AberagePrice column(first 5 elements)

albany_df = df[df[ df['region'] == "Albany"]]
print(albany_df)
print(albany_df.index)

