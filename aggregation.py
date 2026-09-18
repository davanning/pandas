import pandas as pd

data = {
    "Class": ["A", "B", "A", "B", "C", "C"],
    "Score": [85, 90, 78, 92, 88, 95],
    "Age": [20, 21, 19, 22, 20, 23]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 50)

# Grouping the DataFrame by the "Class" column and calculating the mean of the "Score" and "Age" columns for each class.
grouped = df.groupby("Class").mean()
print("Grouped DataFrame (mean):")
print(grouped)
print("-" * 50)

# calculating multiple aggregation functions (mean, max, min) for the "Score" and "Age" columns for each class.

stats = df.groupby("Class").agg({
    "Score": ["mean", "max", "min", "median"],
    "Age": ["mean", "max", "min", "median"]
})

print("Aggregated DataFrame (mean, max, min, median):")
print(stats)
print("-" * 50)