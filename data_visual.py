import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

del df['species']

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# data = np.random.rand(5,5)
# # sns.heatmap(data, annot=True, cmap='coolwarm')
# # plt.title('Heatmap Example')
# sns.kdeplot(np.random.rand(1000), shade=True, color='r')
# plt.title('KDE Plot Example')
# plt.show()


# basic Plot
# x = [1, 2, 3, 4, 5]
# y = [20, 32, 52, 71, 11]
# plt.plot(x, y)
# plt.show()

# Line Plot
# plt.plot([1, 2, 3, 4, 5], [20, 32, 52, 71, 11], label='Data', color='blue', marker='o')
# plt.title('Data Visualization')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()

# Bar Chart
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [20, 32, 52, 71, 11]
# plt.bar(categories, values, color='orange')
# plt.title('Bar Chart')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.show()

# Histogram
# data = [20, 32, 52, 71, 11, 25, 30, 45, 60, 80]
# plt.hist(data, bins=5, color='green', edgecolor='black')
# plt.title('Histogram')
# plt.xlabel('Value Ranges')
# plt.ylabel('Frequency')
# plt.show()

# Scatter Plot
# x = [1, 2, 3, 4, 5]
# y = [20, 32, 52, 71, 11]
# plt.scatter(x, y, color='red')
# plt.title('Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.legend(['Data Points'])
# plt.show()

# Line Plot with Multiple Lines
# x = [1, 2, 3, 4, 5]
# y1 = [20, 32, 52, 71, 11]
# y2 = [15, 25, 35, 45, 55]
# plt.plot(x, y1, label='Data 1', color='blue', marker='o')
# plt.plot(x, y2, label='Data 2', color='orange', marker='s')
# plt.title('Line Plot with Multiple Lines')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()

# Pie Chart
# labels = ['A', 'B', 'C', 'D', 'E']
# sizes = [20, 32, 52, 71, 11]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title('Pie Chart')
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# plt.show()

