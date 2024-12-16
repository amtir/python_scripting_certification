import numpy as np

# Path to the CSV file
file_path = 'SalaryGender.csv'

# Use numpy.genfromtxt to read the data, skipping the header row
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

# Extract each column into a separate NumPy array
# Ensuring salaries are treated as floats
salaries = data[:, 0].astype(float)  # Already float by default, but emphasizing for clarity
genders = data[:, 1].astype(int)  # Convert to int for consistency
ages = data[:, 2].astype(int)  # Convert to int for consistency
phds = data[:, 3].astype(int)  # Convert to int for consistency

# Print the arrays (optional)
print("Salaries:", salaries)
print("Genders:", genders)
print("Ages:", ages)
print("PhDs:", phds)

# Number of men with a PhD
men_with_phd = np.sum((genders == 1) & (phds == 1))

# Number of women with a PhD
women_with_phd = np.sum((genders == 0) & (phds == 1))

# Print the results
print("Number of men with a PhD:", men_with_phd)
print("Number of women with a PhD:", women_with_phd)