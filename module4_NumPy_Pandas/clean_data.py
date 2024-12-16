import pandas as pd

def convert_k_to_number(value):
    try:
        value_str = str(value)
        if 'k' in value_str:
            return float(value_str.replace('k', '')) * 1000
        return float(value_str)
    except ValueError:
        return value

# Load the dataset
income = pd.read_csv('income.csv')

# Apply the conversion only to numeric columns
for column in income.columns[1:]:
    income[column] = income[column].apply(convert_k_to_number)

# Save the cleaned dataset
income.to_csv('cleaned_income.csv', index=False)

print("Data cleaned and saved successfully.")
