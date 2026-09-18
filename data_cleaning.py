import pandas as pd

data = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [25, None, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago", None]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# Fill missing value with interpolation mehtod
df["Age"] = df["Age"].interpolate()
print("\nDataFrame after interpolation:")
print(df)



# # Fill missing values with backward fill method
# df = df.bfill()
# print("\nDataFrame after backward filling missing values:")
# print(df)

# Fill missing values with forward fill method
# print("\nDataFrame after forward filling missing values:")
# print(df)

# df = df.fillna({
#     "Name": "Unknown",
#     "Age": df["Age"].mean(),
#     "City": "Unknown"
# })
# print("\nDataFrame after filling missing values:")
# print(df)


# # Drop rows with missing values
# df = df.dropna() 
# print("\nDataFrame after dropping rows with missing values:")
# print(df)

# # Drop columns with missing values
# df = df.dropna(axis=1)
# print("\nDataFrame after dropping rows and columns with missing values:")
# print(df)

# df = df.fillna({
#     "Name": "Unknown",
#     "Age": df["Age"].mean(),
#     "City": "Unknown"
# })
# print("\nDataFrame after filling missing values:")
# print(df)


# df.fillna(method='bfill')

# df["column_name"] = df["column_name"].interpolate()