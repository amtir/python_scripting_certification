
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# Load the dataset
income = pd.read_csv('cleaned_income.csv')

# Display the first few rows to understand its structure
print(income.head())


# Assuming 2022 is a column in the dataset
top_10_2022 = income[['country', '2022']].sort_values(by='2022', ascending=False).head(10)
print("\nTop 10 countries in 2022:")
print(top_10_2022)


# Find the richest country for each year-----------------------
richest_each_year = income.set_index('country').idxmax()

# Count the occurrences of each country being the richest
richest_counts = richest_each_year.value_counts()
print("\nRitchest countries:")
print(richest_counts)


# Find the poorest country for each year-------------------------
poorest_each_year = income.set_index('country').idxmin()

# Count the occurrences of each country being the poorest
poorest_counts = poorest_each_year.value_counts()
print("\nPoorest countries:")
print(poorest_counts)



# Calculate the gap between the minimum and maximum income for each year -------------------
income_gap = income.drop(columns=['country']).max() - income.drop(columns=['country']).min()

# Plot the income gap over time
plt.figure(figsize=(12, 6))
income_gap.plot()
plt.title('Gap between the minimum and maximum income over time')
plt.xlabel('Year')
plt.ylabel('Income Gap')
plt.show()
