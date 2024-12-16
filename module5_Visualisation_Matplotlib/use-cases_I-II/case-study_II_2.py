import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the data
# Load the data
data = pd.read_csv('BigMartSalesData.csv')

# Convert InvoiceDate to datetime format
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%y')

# Filter data for the year 2011
data_2011 = data[data['InvoiceDate'].dt.year == 2011].copy()

# Ensure all columns are in correct types
data_2011['Month'] = data_2011['InvoiceDate'].dt.month
data_2011['Country'] = data_2011['Country'].astype('category')

# Preview the data
print(data_2011.head())

# Group by month and calculate total sales
monthly_sales = data_2011.groupby('Month')['Amount'].sum()

# Step 2: Plot Total Sales Per Month for Year 2011
# Plot Total Sales Per Month
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Total Sales Per Month for Year 2011')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Identify the month with the lowest sales
lowest_sales_month = monthly_sales.idxmin()
print(lowest_sales_month)

# Step 3: Plot Total Sales Per Month for Year 2011 as Bar Chart
# Bar Chart of Total Sales Per Month
plt.figure(figsize=(10, 6))
bars = plt.bar(monthly_sales.index, monthly_sales.values, color='skyblue')
plt.title('Total Sales Per Month for Year 2011')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Adding value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5000, int(yval), ha='center', va='bottom')

plt.show()

# Step 4: Plot Pie Chart for Year 2011 Country Wise
# Group by country and calculate total sales
country_sales = data_2011.groupby('Country')['Amount'].sum()

# Plot Pie Chart for Country Wise Sales
plt.figure(figsize=(12, 8))
plt.pie(country_sales, labels=country_sales.index, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Country Wise Sales Distribution for Year 2011')
plt.axis('equal')
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()

# Identify the country with the highest sales
highest_sales_country = country_sales.idxmax()
print(highest_sales_country)

# Step 5: Plot Scatter Plot for the Invoice Amounts
# Scatter Plot for Invoice Amounts
plt.figure(figsize=(10, 6))
plt.scatter(data_2011.index, data_2011['Amount'], alpha=0.5, color='red')
plt.title('Scatter Plot of Invoice Amounts for Year 2011')
plt.xlabel('Invoice Index')
plt.ylabel('Invoice Amount')
plt.show()

# Analyze the concentration of invoice amounts
invoice_amount_range = data_2011['Amount'].value_counts(bins=10).sort_index()
print(invoice_amount_range)

# Step 6: Display the results
# Display the data frame for analysis
# tools.display_dataframe_to_user(name="BigMart 2011 Sales Data", dataframe=data_2011)
