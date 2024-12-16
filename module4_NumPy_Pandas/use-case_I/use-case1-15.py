import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('middle_tn_schools.csv')

# Display the first few rows of the data
print(data.head())

# Describe the data
data_description = data.describe(include='all')
print(data_description)


# Group data by school_rating and describe the reduced_lunch variable
grouped_data = data.groupby('school_rating')['reduced_lunch'].describe()
print(grouped_data)


# Phase 3 - Correlation Analysis
correlation = data['reduced_lunch'].corr(data['school_rating'])
print(f"Correlation: {correlation}")


# Phase 4 - Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['reduced_lunch'], data['school_rating'])
plt.title('Scatter Plot of School Rating vs. Reduced Lunch')
plt.xlabel('Percentage of Students on Reduced Lunch')
plt.ylabel('School Rating')
plt.grid(True)
plt.show()


# Phase 5 - Correlation Matrix
# Select only numeric columns
numeric_data = data.select_dtypes(include=[float, int])

# Compute the correlation matrix
plt.figure(figsize=(12, 10))
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()


