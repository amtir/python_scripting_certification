import pandas as pd

# Load the CSV files
math_scores = pd.read_csv('MathScoreTerm1.csv')
physics_scores = pd.read_csv('PhysicsScoreTerm1.csv')

# Display summary information about each dataset
print("Math Scores Summary:")
print(math_scores.describe(include='all'))

print("\nPhysics Scores Summary:")
print(physics_scores.describe(include='all'))

# Remove the Name and Ethnicity columns from math_scores and physics_scores
math_scores = math_scores.drop(columns=['Name', 'Ethinicity'])
physics_scores = physics_scores.drop(columns=['Name', 'Ethinicity'])

# Fill missing score data with zero
math_scores['Score'] = math_scores['Score'].fillna(0)
physics_scores['Score'] = physics_scores['Score'].fillna(0)

# Merge the math_scores and physics_scores on ID, Age, Subject, and Sex
merged_scores = pd.merge(math_scores, physics_scores, on=['ID', 'Age', 'Sex'], suffixes=('_Math', '_Physics'))

# Change Sex(M/F) column to 1/2 for further analysis
merged_scores['Sex'] = merged_scores['Sex'].map({'M': 1, 'F': 2})

# Store the data in a new file – ScoreFinal.csv
merged_scores.to_csv('MergeScoreFinal.csv', index=False)

print("Processing and merging completed. The final merged file is saved as MergeScoreFinal.csv.")
