""""
What is Pandas ?
Pandas is a powerful and widely-used open-source data manipulation and analysis library for Python. It provides data structures and functions needed to manipulate structured data seamlessly. The primary data structures in Pandas are Series (1-dimensional) and DataFrame (2-dimensional), which allow for efficient handling of large datasets.

Pandas Data Structures:
1. Series: A one-dimensional labeled array that can hold any data type (integers, strings, floating-point numbers, etc.). Each element in a Series has an associated label (index) that allows for easy access and manipulation.
2. DataFrame: A two-dimensional labeled data structure that can hold data of different types (like a table). It consists of rows and columns, where each column can be of a different data type. DataFrames are particularly useful for handling and analyzing tabular data.
"""
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)

data = {
    "Name": ["Alice", "Bob", "Charlie"], 
    "Age": [25, 30, 35], 
    "City": ["New York", "Los Angeles", "Chicago"]
    }
df = pd.DataFrame(data)
print(df)


