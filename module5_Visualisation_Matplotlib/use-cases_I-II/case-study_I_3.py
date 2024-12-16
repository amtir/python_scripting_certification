import pandas as pd
import matplotlib.pyplot as plt

# Assuming the CSV data is loaded into a DataFrame
data = pd.read_csv('Cars2015.csv')

# Count the number of models for each manufacturer
model_counts = data['Make'].value_counts()

largest_releases_manufacturer = model_counts.idxmax()
print(f"The manufacturer with the largest releases is {largest_releases_manufacturer} with {model_counts.max()} models.")

# Plot the pie chart
plt.figure(figsize=(10, 8))
plt.pie(model_counts, labels=model_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Models Released by Each Manufacturer in 2015')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()


