import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('CityTemps.csv')

# Plot the histograms
plt.figure(figsize=(14, 6))

# Histogram for Moscow
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.hist(data['Moscow'], bins=20, color='blue', alpha=0.7)
plt.title('Temperature Distribution in Moscow (2014-2015)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Histogram for San Francisco
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.hist(data['San Francisco'], bins=20, color='green', alpha=0.7)
plt.title('Temperature Distribution in San Francisco (2014-2015)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()  # Display the plots