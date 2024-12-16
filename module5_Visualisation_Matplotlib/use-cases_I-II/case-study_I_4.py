import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'sample-salesv2.csv' is the file name
data = pd.read_csv('sample-salesv2.csv')

# Phase 2: Describe the data on the unit price
unit_price_description = data['unit price'].describe()
print(unit_price_description)

# Phase 3: Filter the data and create a new DataFrame
filtered_data = data[['name', 'net_price', 'date']]
grouped_data = filtered_data.groupby('name').sum().reset_index()
print(grouped_data)

# Phase 4: Plotting Graph
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['name'], grouped_data['net_price'])
plt.xlabel('Name')
plt.ylabel('Total Net Price')
plt.title('Total Net Price by Name')
plt.xticks(rotation=90)

plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()  # Display the plots


