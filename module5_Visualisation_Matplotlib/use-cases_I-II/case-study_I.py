import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
data = pd.read_csv('Hurricanes.csv')

# Step 2: Plot the data
plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.bar(data['Year'], data['Hurricanes'], color='blue')  # Create a bar graph
plt.title('Number of Hurricanes per Year')  # Title of the graph
plt.xlabel('Year')  # Label for the x-axis
plt.ylabel('Number of Hurricanes')  # Label for the y-axis
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()  # Display the plot