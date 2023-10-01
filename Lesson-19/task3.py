import seaborn as sns
import matplotlib.pyplot as plt

# Plot Type: Scatter plot
# Use Cases: Visualizing the relationship between two numerical variables.
# Example on the Dataset: Visualize the relationship between total bill and tip amount.
tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# Plot Type: Line plot
# Use Cases: Showing trends or changes in numerical data over time or continuous intervals.
# Example on the Dataset: Visualize the trend of total bill amounts over time.
tips = sns.load_dataset("tips")
sns.lineplot(x="time", y="total_bill", data=tips)
plt.show()

# Plot Type: Bar plot
# Use Cases: Comparing categories and their numerical values.
# Example on the Dataset: Compare the average total bill for different days
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()

# Plot Type: Count plot
# Use Cases: Visualizing the frequency or count of categorical variables.
# Example on the Dataset: Count the number of smokers and non-smokers.
tips = sns.load_dataset("tips")
sns.countplot(x="smoker", data=tips)
plt.show()

# Plot Type: Box plot
# Use Cases: Visualizing the distribution and spread of numerical data and identifying outliers.
# Example on the Dataset: Visualize the distribution of total bills by day.
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# Plot Type: Histogram
# Use Cases: Showing the distribution of numerical data.
# Example on the Dataset: Visualize the distribution of total bill amounts.
tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"])
plt.show()