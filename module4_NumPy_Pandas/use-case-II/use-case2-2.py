import pandas as pd

# Load the CSV files
math_scores = pd.read_csv('MathScoreTerm1.csv')
physics_scores = pd.read_csv('PhysicsScoreTerm1.csv')
ds_scores = pd.read_csv('ScoreFinal.csv')

# Remove the Name and Ethinicity columns from math_scores, physics_scores, and ds_scores
math_scores = math_scores.drop(columns=['Name', 'Ethinicity'])
physics_scores = physics_scores.drop(columns=['Name', 'Ethinicity'])
#ds_scores = ds_scores.drop(columns=['Name', 'Ethinicity'])

# Fill missing score data with zero
math_scores['Score'] = math_scores['Score'].fillna(0)
physics_scores['Score'] = physics_scores['Score'].fillna(0)
ds_scores['Score'] = ds_scores['Score'].fillna(0)

# Merge the math_scores, physics_scores, and ds_scores on ID, Age, and Sex
merged_scores = pd.merge(math_scores, physics_scores, on=['ID', 'Age', 'Sex'], suffixes=('_Math', '_Physics'))
merged_scores = pd.merge(merged_scores, ds_scores, on=['ID', 'Age', 'Sex'], suffixes=('', '_DS'))

# Rename columns to avoid confusion
merged_scores.rename(columns={'Score': 'Score_DS', 'Subject': 'Subject_DS'}, inplace=True)

# Change Sex(M/F) column to 1/2 for further analysis
merged_scores['Sex'] = merged_scores['Sex'].map({'M': 1, 'F': 2})

# Store the data in a new file – ScoreFinal.csv
merged_scores.to_csv('MergedScoreFinal.csv', index=False)

print("Processing and merging completed. The final merged file is saved as ScoreFinal.csv.")
