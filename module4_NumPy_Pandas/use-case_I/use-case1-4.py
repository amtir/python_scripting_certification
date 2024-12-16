import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('SalaryGender.csv')

# Filter the DataFrame to keep only those with a PhD
df_with_phd = df[df['PhD'] == 1]

# Select only the "Age" and "PhD" columns
age_phd_df = df_with_phd[['Age', 'PhD']]

# Display the resulting DataFrame
#print(age_phd_df)

# Calculate the total number of people with a PhD
total_phd = len(df_with_phd)

# Print the total number
print("Total number of people with a PhD:", total_phd)





