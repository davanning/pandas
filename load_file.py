import pandas as pd

# load data from csv file
df = pd.read_csv('data.csv')
# print(df)
df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)

# view data
print(df.head())
print("-----------------------------")
print(df.tail(2))
print("-----------------------------")
print(df.info())
print("-----------------------------")
print(df.describe())

# filter data
filtered_df = df[df['age'] > 2000]
print(filtered_df)

print("-----------------------------")
print(df.iloc[0])  # first row
print("-----------------------------")
print(df.loc[1:2])  # second and third row