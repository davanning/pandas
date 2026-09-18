""""
Combine data cleaning techniques to handle missing values in a DataFrame. This code demonstrates how to drop rows and columns with missing values, as well as how to fill missing values using forward fill method. The original DataFrame is printed before and after each cleaning step to show the changes made to the data.
"""

# concat() function to combine two DataFrames
# merge() function to combine two DataFrames based on a common column
# join() function to combine two DataFrames based on their index

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

df = pd.DataFrame({
    "ID": [2, 3, 4],
    "Age": [25, 30, 22]
})

# concat() function to combine two DataFrames
# By default, it concatenates along the rows (axis=0), but you can specify axis=1 to concatenate along the columns.
# reindex = pd.concat([df1, df], ignore_index=True)
# print(reindex)
# print("-" * 50)
# result = pd.concat([df1, df], axis=1)
# print(result)

# how parameter in merge() function specifies the type of merge to be performed. It can take the following values:
# 'left': Use keys from left DataFrame only
# 'right': Use keys from right DataFrame only
# 'outer': Use union of keys from both DataFrames
# 'inner': Use intersection of keys from both DataFrames
result = pd.merge(df1, df, on="ID", how="left")
# print(result)

# join() function to combine two DataFrames based on their index
# By default, it performs a left join, but you can specify how='right', how='outer', or how='inner' to change the type of join.

# set_index() method is used to set the DataFrame index using one or more existing columns. In this case, we are setting the index to the "ID" column before performing the join operation. This allows us to combine the two DataFrames based on their index values.
result = df1.set_index("ID").join(df.set_index("ID"), how="left")
print(result)

""""
🔥 Visual Summary
concat  → stacking tables
merge   → database join using column
join    → merge using index
"""